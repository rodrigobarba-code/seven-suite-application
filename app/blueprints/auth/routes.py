from . import auth_bp
from flask import render_template, redirect, url_for, flash, request, session
from app.blueprints.users.models import User
import bcrypt
from app.decorators import RequirementsDecorators as restriction


# Login Route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password').encode('utf-8')  # Encode the password to bytes
        user = User.query.filter_by(user_username=username).first()
        if user:
            print(f"User found: {user.user_username}")
            if bcrypt.checkpw(password, user.user_password):  # Check the password hash
                print("Password is correct")
                session['user_id'] = user.user_id
                session['user_privileges'] = user.user_privileges  # Ensure this line is present
                session['user_name'] = user.user_name
                session['user_lastname'] = user.user_lastname  # Add this line
                if user.user_privileges == 'admin':
                    session['user_avatar'] = url_for('static', filename='img/user_avatars/admin_avatar.svg')
                elif user.user_privileges == 'employee':
                    session['user_avatar'] = url_for('static', filename='img/user_avatars/user_avatar.svg')
                elif user.user_privileges == 'guest':
                    session['user_avatar'] = url_for('static', filename='img/user_avatars/guest_avatar.svg')
                return redirect(url_for('home.home'))
            else:
                print("Password is incorrect")
                flash('Invalid username or password')
        else:
            print("User not found")
            flash('Invalid username or password')
    return render_template('auth/login.html')


# Log out Route
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))


# Example of a protected route
@auth_bp.route('/protected')
@restriction.login_required
def protected():
    return 'This is a protected route'
