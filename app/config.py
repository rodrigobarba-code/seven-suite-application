# Importing OS module to generate a random secret key
import os
# Importing OS module to generate a random secret key

# Config class to store all the configurations of the database
class DatabaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLALCHEMY_TRACK_MODIFICATIONS too False to suppress warning
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///seven_suite.db'  # Database URI for the app
# Config class to store all the configurations of the database

# Config class to store all the configurations of the application
class AppConfig:
    PORT = 5000  # Port number for the app
    DEBUG = True  # Debug mode for the app
    SECRET_KEY = os.urandom(24)  # Secret key for the app
# Config class to store all the configurations of the application
