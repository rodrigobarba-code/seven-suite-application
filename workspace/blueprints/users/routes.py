# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import users_bp
import workspace
# Importing Required Libraries

from workspace.models.model_users import ModelUsers
from workspace.models.entities.user import User




# Main Route
@users_bp.route('/')
def users():
    return render_template('public/users/users.html')


# Main Route

# Add User Route
@users_bp.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user = User(
            user_id=0,
            username=request.form['username'],
            password=request.form['password'],
            name=request.form['name'],
            lastname=request.form['lastname'],
            privileges=request.form['privileges']
        )
        try:
            ModelUsers.add_user(workspace.db, user)
            flash('User Added Successfully', 'success')
            return redirect(url_for('users.users'))
        except Exception as e:
            flash("{error_message}".format(error_message=str(e)), 'danger')
            return redirect(url_for('users.users'))
    return render_template('public/users/form_users.html', user=None)
# Add User Route
