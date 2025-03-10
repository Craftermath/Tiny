# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


db: SQLAlchemy = SQLAlchemy()
cache: Cache = Cache()

def create_app():
    app: Flask = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tinyurl.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CACHE_TYPE'] = 'SimpleCache'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = 'choose_another_password_here'   # Flask-WTF

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app)

    # Register blueprints
    from .views import main_blueprint
    app.register_blueprint(main_blueprint)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
