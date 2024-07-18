# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
auth_bp = Blueprint('auth', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes
