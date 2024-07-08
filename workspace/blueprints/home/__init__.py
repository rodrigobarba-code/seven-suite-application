# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
home_bp = Blueprint('home', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes
