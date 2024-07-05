# Blueprints
from blueprints.main import main_bp
from blueprints.regions import regions_bp
# Blueprints

# Flask import
from flask_mysqldb import MySQL
from flask import *
# Flask import

db = MySQL()


def create_app():
    # Create Flask application
    application = Flask(__name__)
    # Create Flask application

    # Create Database connection
    db.init_app(application)
    # Create Database connection

    # Register Blueprints
    application.register_blueprint(main_bp, url_prefix='/')
    application.register_blueprint(regions_bp, url_prefix='/regions')
    # Register Blueprints

    return application
