# Importing Required Libraries
from . import dashboard_bp
from flask import render_template, redirect, url_for, flash, request, jsonify
# Importing Required Libraries

# Dashboard Main Route
@dashboard_bp.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard/dashboard.html')
# Dashboard Main Route
