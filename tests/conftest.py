# tests/conftest.py

import pytest
from app import create_app
from app.models import URL, db as _db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False 
    app.config['SECRET_KEY'] = 'ifoudvlvfhcoiredavfjoefidsa' 

    with app.app_context():
        _db.create_all()

    yield app

    with app.app_context():
        _db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def db(app):
    """Provide access to the database."""
    with app.app_context():
        yield _db
