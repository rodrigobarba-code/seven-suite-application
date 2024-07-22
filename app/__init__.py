# Importing Flask, Configurations and App Extensions
from flask import Flask
from app.extensions import db, migrate
from app.config import DatabaseConfig, AppConfig
# Importing Flask, Configurations and App Extensions

# Importing Blueprints
from app.blueprints.home import home_bp
from app.blueprints.regions import regions_bp
from app.blueprints.dashboard import dashboard_bp
# Importing Blueprints

# Function constructor to create the app
def create_app():
    app = Flask(__name__)  # Creating the app

    app.config.from_object(AppConfig)  # Setting the application configurations
    app.config.from_object(DatabaseConfig)  # Setting the database configurations

    db.init_app(app)  # Initializing the database
    migrate.init_app(app, db)  # Initializing the migration

    # Registering the blueprints
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(regions_bp, url_prefix='/regions')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    # Registering the blueprints

    return app  # Returning the app
# Function constructor to create the app
