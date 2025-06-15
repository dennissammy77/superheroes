import pytest
from app import app
from models import db

@pytest.fixture(scope='session')
def test_app():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.app_context():
        yield app

@pytest.fixture(scope='function')
def test_db(test_app):
    with test_app.app_context():
        db.create_all()
        yield db
        db.session.rollback()
        db.drop_all()
