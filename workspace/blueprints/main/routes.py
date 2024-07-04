# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import main_bp
# Importing Required Libraries


# Main Route
@main_bp.route('/')
def index():
    return render_template('public/main/index.html')
# Main Route
