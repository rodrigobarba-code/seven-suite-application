# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
users_bp = Blueprint('users', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes
