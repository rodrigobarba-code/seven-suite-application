# Importing Required Libraries
from . import home_bp
from flask import render_template, redirect, url_for, flash, request, jsonify
from app.decorators import RequirementsDecorators as restriction


# Importing Required Libraries

# Home Main Route
@home_bp.route('/', methods=['GET'])
@restriction.login_required
def home():
    return render_template('home/home.html')
# Home Main Route
