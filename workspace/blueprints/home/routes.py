# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import home_bp
# Importing Required Libraries


# Main Route
@home_bp.route('/')
def home():
    return render_template('public/home/home.html')
# Main Route
