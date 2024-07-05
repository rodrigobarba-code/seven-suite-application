# Import Creation Function from __init__.py
from __init__ import create_app
from config import DevelopmentConfig
# Import Creation Function from __init__.py

# Create Flask application
app = create_app()
# Create Flask application

# Run Flask application
if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(port=3000, debug=True)
# Run Flask application
