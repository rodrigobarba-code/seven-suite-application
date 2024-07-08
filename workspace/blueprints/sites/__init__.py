# Import Blueprint
from flask import Blueprint
# Import Blueprint

# Create Blueprint
sites_bp = Blueprint('sites', __name__, template_folder='templates')
# Create Blueprint

# Import routes
from . import routes
# Import routes
