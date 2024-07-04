# Imports
from config import DevelopmentConfig
# Imports

# Blueprints
from blueprints.main import main_bp
from blueprints.regions import regions_bp
# Blueprints

# Flask import
from flask_mysqldb import MySQL
from flask import *
# Flask import


def create_app():
    # Create Flask application
    application = Flask(__name__)
    application.config.from_object(Config)
    # Create Flask application

    # Create Database connection
    db = MySQL(application)
    db.init_app(application)
    # Create Database connection

    # Register Blueprints
    application.register_blueprint(main_bp, url_prefix='/')
    application.register_blueprint(regions_bp, url_prefix='/regions')
    # Register Blueprints

    return application
