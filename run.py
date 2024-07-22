# Importing main application constructor
from app import create_app
from app.config import AppConfig
# Importing main application constructor

# Creating application instance
app = create_app()
# Creating application instance

# Running application
if __name__ == '__main__':
    app.run(port=AppConfig.PORT, debug=AppConfig.DEBUG)  # Running the app with the configurations
# Running application
