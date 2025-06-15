from app import app
from models import HeroPower,Hero, Power, db

class TestHeroPower:
    '''Test model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        r = HeroPower()
        assert r
        assert isinstance(r, HeroPower)

    def test_has_strength(self):
        '''can be instantiated with a strength attribute.'''
        r = HeroPower(strength='Average')
        assert r.strength == 'Average'

    def test_has_hero_id(self):
        '''can be instantiated with a hero_id attribute.'''
        r = HeroPower(hero_id=1)
        assert r.hero_id == 1

    def test_has_power_id(self):
        '''can be instantiated with a power_id attribute.'''
        r = HeroPower(power_id=1)
        assert r.power_id == 1

    def test_can_be_saved_to_database(self):
        '''can be added to a transaction and committed to HeroPowers table with strength, hero_id and power_id column.'''
        with app.app_context():
            assert 'strength' in HeroPower.__table__.columns
            assert 'hero_id' in HeroPower.__table__.columns
            assert 'power_id' in HeroPower.__table__.columns
            r = HeroPower(strength='Average',hero_id=1,power_id=1)
            db.session.add(r)
            db.session.commit()
            assert hasattr(r, 'id')
            assert db.session.query(HeroPower).filter_by(id=r.id).first()