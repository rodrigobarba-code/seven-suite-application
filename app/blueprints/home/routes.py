# Importing Required Libraries
from . import home_bp
from flask import render_template, redirect, url_for, flash, request, jsonify
# Importing Required Libraries

# Home Main Route
@home_bp.route('/', methods=['GET'])
def home():
    return render_template('home/home.html')
# Home Main Route
