from app import app
from models import Power, db

class TestPower:
    '''Test model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        r = Power()
        assert r
        assert isinstance(r, Power)

    def test_has_name(self):
        '''can be instantiated with a name attribute.'''
        r = Power(name='super strength')
        assert r.name == 'super strength'

    def test_has_description(self):
        '''can be instantiated with a description attribute.'''
        r = Power(description='gives the wielder super-human strengths')
        assert r.description == 'gives the wielder super-human strengths'

    def test_can_be_saved_to_database(self):
        '''can be added to a transaction and committed to Powers table with name and description column.'''
        with app.app_context():
            assert 'name' in Power.__table__.columns
            assert 'description' in Power.__table__.columns
            r = Power(name='super strength',description='gives the wielder super-human strengths')
            db.session.add(r)
            db.session.commit()
            assert hasattr(r, 'id')
            assert db.session.query(Power).filter_by(id=r.id).first()