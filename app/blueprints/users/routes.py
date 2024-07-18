from flask import render_template, redirect, url_for, flash, request
from app.blueprints.users import users_bp
from app.forms import UserForm
from app.models import User
from app.extensions import db

@users_bp.route('/')
def user_index():
    users = User.query.all()
    return render_template('users/user_list.html', users=users)

@users_bp.route('/user/new', methods=['GET', 'POST'])
@users_bp.route('/user/<int:user_id>/edit', methods=['GET', 'POST'])
def user_form(user_id=None):
    form = UserForm()
    if user_id:
        user = User.query.get_or_404(user_id)
        if request.method == 'GET':
            form.username.data = user.username
            form.email.data = user.email
    else:
        user = User()

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()
        flash('User saved successfully!', 'success')
        return redirect(url_for('users.user_index'))

    return render_template('users/user_form.html', form=form, user_id=user_id)

@users_bp.route('/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('users.user_index'))
