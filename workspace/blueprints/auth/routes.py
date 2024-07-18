# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import auth_bp
# Importing Required Libraries


# Main Route
@auth_bp.route('/')
def login():
    return render_template('public/auth/login.html')
# Main Route
