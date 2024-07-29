from functools import wraps
from flask import session, redirect, url_for


class RequirementsDecorators:
    @staticmethod
    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)

        return decorated_function

    # Create a new decorator for admin privileges knowing that the admin user is the one with 'admin' privileges
    @staticmethod
    def admin_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_privileges' not in session or session['user_privileges'] != 'admin':
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)

        return decorated_function
