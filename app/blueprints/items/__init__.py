from flask import Blueprint

items_bp = Blueprint('items', __name__, template_folder='templates')

from app.blueprints.items import routes
