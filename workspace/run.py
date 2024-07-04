# Import Creation Function from __init__.py
from __init__ import create_app
# Import Creation Function from __init__.py

# Create Flask application
app = create_app()
# Create Flask application

# Run Flask application
if __name__ == '__main__':
    app.run(port=3000, debug=True)
# Run Flask application
