# Import Creation Function from __init__.py
from workspace import create_app
from workspace.config import DevelopmentConfig
# Import Creation Function from __init__.py


# Create Flask application
app = create_app()
# Create Flask application


# Run Flask application
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(port=3000)
# Run Flask application
