# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import users_bp
# Importing Required Libraries


# Main Route
@users_bp.route('/')
def users():
    return render_template('public/users/users.html')
# Main Route
