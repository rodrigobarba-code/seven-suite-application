# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request, jsonify
from . import users_bp
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.users.entities import UserEntity
# Importing Required Entities

# Importing Required Models
from app.blueprints.users.models import User


# Importing Required Models

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
    print(user_ids)
    try:
        for user_id in user_ids:
            User.delete_user(user_id)
        flash('Users Deleted Successfully', 'success')
        return jsonify({'message': 'Users deleted successfully'}), 200
    except Exception as e:
        flash(str(e), 'danger')
        return jsonify({'message': 'Failed to delete users', 'error': str(e)}), 500
# Users Bulk Delete Route

# Routers Delete All Route
@users_bp.route('/delete_all_users', methods=['POST'])
def delete_all_users():
    try:
        User.delete_all_users()
        flash('All Routers Deleted Successfully', 'success')
        return jsonify({'message': 'Routers deleted successfully'}), 200
    except Exception as e:
        flash(str(e), 'danger')
        return jsonify({'message': 'Failed to delete routers', 'error': str(e)}), 500
# Routers Delete All Route
