# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
main_bp = Blueprint('main', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes
