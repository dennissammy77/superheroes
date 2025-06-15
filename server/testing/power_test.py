import pytest
from app import app
from models import Hero, Power, HeroPower, db

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

    def test_hero_powers_relationship(self):
        '''can be get hero_powers .'''
        with app.app_context():
            Khan = Hero(name='Kamala Khan',super_name='Ms. Marvel')
            super_strength = Power(name='super strength',description='gives the wielder super-human strengths')
            db.session.add_all([Khan,super_strength])
            db.session.commit()

            h_p = HeroPower(strength='Average',hero_id=Khan.id,power_id=super_strength.id)
            db.session.add(h_p)
            db.session.commit()


            assert db.session.query(Power).filter_by(id=super_strength.id).first().hero_powers == [h_p]

    def test_description_length_validation(self):
        '''Raises ValueError if description is short'''
        with pytest.raises(ValueError) as excinfo:
            Power(description='I am short')
        assert "Description must be at least 20 characters long." in str(excinfo.value)