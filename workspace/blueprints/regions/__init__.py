# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
regions_bp = Blueprint('regions', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes
