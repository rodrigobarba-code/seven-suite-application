# Import necessary modules
import os
# Import necessary modules


# Development configurations
class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'seven_suite'
    # Add other development configurations here
# Development configurations


# Production configurations
class ProductionConfig:
    DEBUG = False
    # Add other production configurations here
# Production configurations


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
# Configuration dictionary
