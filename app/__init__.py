from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.blueprints.items import items_bp
from app.blueprints.users import users_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(items_bp, url_prefix='/items')
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
