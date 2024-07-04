# Importing Required Libraries
from flask import render_template, redirect, url_for, flash, request
from . import regions_bp
# Importing Required Libraries


# Main Route
@regions_bp.route('/')
def regions():
    return render_template('public/regions/regions.html')
# Main Route
