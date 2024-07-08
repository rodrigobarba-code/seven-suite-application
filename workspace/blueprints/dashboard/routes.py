# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import dashboard_bp
# Importing Required Libraries


# Main Route
@dashboard_bp.route('/')
def dashboard():
    return render_template('public/dashboard/dashboard.html')
# Main Route
