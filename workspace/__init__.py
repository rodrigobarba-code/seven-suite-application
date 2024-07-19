# Blueprints import
from blueprints.home import home_bp
from blueprints.sites import sites_bp
from blueprints.regions import regions_bp
from blueprints.routers import routers_bp
from blueprints.dashboard import dashboard_bp
from blueprints.users import users_bp
# Blueprints import


# Flask import
from flask_mysqldb import MySQL
from flask import *
# Flask import


# Database connection
db = MySQL()
# Database connection


# Function to create Flask application
def create_app():
    # Create Flask application
    application = Flask(__name__)
    # Create Flask application

    # Create Database connection
    db.init_app(application)
    # Create Database connection

    # Register Blueprints
    application.register_blueprint(home_bp, url_prefix='/')
    application.register_blueprint(users_bp, url_prefix='/users')
    application.register_blueprint(sites_bp, url_prefix='/sites')
    application.register_blueprint(regions_bp, url_prefix='/regions')
    application.register_blueprint(routers_bp, url_prefix='/routers')
    application.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    # Register Blueprints

    # Return application
    return application
    # Return application
