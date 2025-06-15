from app import app, db
from server.models import Hero


class TestHero:
    '''Review model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        r = Hero()
        assert r
        assert isinstance(r, Hero)