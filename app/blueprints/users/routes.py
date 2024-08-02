# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request, jsonify, session
from datetime import datetime
from . import users_bp
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.users.entities import UserEntity
from app.blueprints.users.entities import UserLogEntity
# Importing Required Entities

# Importing Required Models
from app.blueprints.users.models import User
from app.blueprints.users.models import UserLog
# Importing Required Models

# Importing Required Functions
from . functions import users_functions as functions
# Importing Required Functions

# Users Main Route
@users_bp.route('/')
def users():
    return render_template(
        'users/users.html',  # Render the users template
        user_list=User.get_users(),  # Pass the user list to the template
        user=None  # Pass None to the template
    )


# Users Main Routea

# Users Add Route
@users_bp.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to add the user
            user = UserEntity(
                user_id=None,  # Set the id to None
                user_username=request.form['user_username'],  # Set the username
                user_password=request.form['user_password'],  # Set the password
                user_name=request.form['user_name'],  # Set the name
                user_lastname=request.form['user_lastname'],  # Set the lastname
                user_privileges=request.form['user_privileges'],  # Set the privileges
                user_state=request.form['user_state']  # Set the status
            )
            User.add_user(user)  # Add the user
            functions.create_log(session['user_id'], 'User added', 'INSERT', 'users')  # Create a log
            flash('User added successfully', 'success')  # Flash a success message
        except Exception as e:  # If an exception occurs
            flash(str(e), 'danger')  # Flash the exception message
        return redirect(url_for('users.users'))
    return render_template(
        'users/form_users.html',  # Render the users template
        user_list=User.get_users(),  # Pass the user list to the template
        user=None  # Pass None to the template
    )


# Users Add Route

# Users Update Route
@users_bp.route('/update/<user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':  # If the request method is POST
        try:  # Try to update the user
            user = UserEntity(
                user_id=user_id,  # Set the id
                user_username=request.form['user_username'],  # Set the username
                user_password=request.form['user_password'],  # Set the password
                user_name=request.form['user_name'],  # Set the name
                user_lastname=request.form['user_lastname'],  # Set the lastname
                user_privileges=request.form['user_privileges'],  # Set the privileges
                user_state=request.form['user_state']  # Set the status
            )
            User.update_user(user)  # Update the user
            functions.create_log(session['user_id'], 'User updated', 'UPDATE', 'users')  # Create a log
            flash('User updated successfully', 'success')  # Flash a success message
        except Exception as e:
            flash(str(e), 'danger')
        return redirect(url_for('users.users'))
    return render_template(
        'users/form_users.html',  # Render the users template
        user_list=User.get_users(),  # Pass the user list to the template
        user=User.get_user(user_id)  # Pass the user to the template
    )


# Users Update Route

# Users Delete Route
@users_bp.route('/delete/<user_id>')
def delete_user(user_id):
    try:  # Try to delete the user
        User.delete_user(user_id)  # Delete the user
        functions.create_log(session['user_id'], 'User deleted', 'DELETE', 'users')  # Create a log
        flash('User deleted successfully', 'success')  # Flash a success message
    except Exception as e:
        flash(str(e), 'danger')
    return redirect(url_for('users.users'))


# User Delete Route

# Users Bulk Delete Route
@users_bp.route('/bulk_delete_user', methods=['POST'])
def bulk_delete_user():
    data = request.get_json()
    user_ids = data.get('users_ids', [])
    try:
        flag = 0
        for user_id in user_ids:
            User.delete_user(user_id)
            flag += 1
        functions.create_log(session['user_id'], f'{flag} Users deleted', 'DELETE', 'users')
        flash('Users Deleted Successfully', 'success')
        return jsonify({'message': 'Users deleted successfully'}), 200
    except Exception as e:
        flash(str(e), 'danger')
        return jsonify({'message': 'Failed to delete users', 'error': str(e)}), 500


# Users Bulk Delete Route

# Users Delete All Route
@users_bp.route('/delete_all_users', methods=['POST'])
def delete_all_users():
    try:
        User.delete_all_users()
        flash('All Routers Deleted Successfully', 'success')
        functions.create_log(session['user_id'], 'All Users deleted', 'DELETE', 'users')
        return jsonify({'message': 'Routers deleted successfully'}), 200
    except Exception as e:
        flash(str(e), 'danger')
        return jsonify({'message': 'Failed to delete routers', 'error': str(e)}), 500


# Users Delete All Route

# Users Log Route
@users_bp.route('/log', methods=['GET'])
def log():
    user_log_list = UserLog.get_user_logs()
    return render_template(
        'users/log.html',
        user_log_list=user_log_list,
        user_functions=User
    )


# Users Log Route

# Users Delete By Date Users Log Route
@users_bp.route('/delete_by_date_user_log', methods=['POST'])
def delete_by_date_user_log():
    data = request.get_json()
    date = data.get('date', None)
    date += ' 23:59:59'
    try:
        UserLog.delete_from_date_user_log(date)
        functions.create_log(session['user_id'], f'User Logs Deleted', 'DELETE', 'user_logs')
        flash('User Logs Deleted Successfully', 'success')
        return jsonify({'message': 'User Logs Deleted Successfully'}), 200
    except Exception as e:
        flash(str(e), 'danger')
        return jsonify({'message': 'User Logs Failed to Delete', 'error': str(e)}), 500
# Users Delete By Date Users Log Route
