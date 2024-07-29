# Importing Required Libraries
from . import dashboard_bp
from flask import render_template, redirect, url_for, flash, request, jsonify
from app.decorators import RequirementsDecorators as restriction


# Importing Required Libraries

# Dashboard Main Route
@dashboard_bp.route('/', methods=['GET'])
@restriction.login_required
def dashboard():
    return render_template('dashboard/dashboard.html')
# Dashboard Main Route
