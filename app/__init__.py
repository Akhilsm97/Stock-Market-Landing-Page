from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from app.routes import add_user, get_users
    app.register_blueprint(add_user)
    app.register_blueprint(get_users)

    with app.app_context():
        db.create_all()  # Create tables at the start

    return app
