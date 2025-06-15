from app import app
from models import Hero, Power, HeroPower, db

class TestHero:
    '''Test model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        r = Hero()
        assert r
        assert isinstance(r, Hero)

    def test_has_name(self):
        '''can be instantiated with a name attribute.'''
        r = Hero(name='Kamala Khan')
        assert r.name == 'Kamala Khan'

    def test_has_super_name(self):
        '''can be instantiated with a super_name attribute.'''
        r = Hero(super_name='Ms. Marvel')
        assert r.super_name == 'Ms. Marvel'

    def test_can_be_saved_to_database(self):
        '''can be added to a transaction and committed to heroes table with name and super_name column.'''
        with app.app_context():
            assert 'name' in Hero.__table__.columns
            assert 'super_name' in Hero.__table__.columns
            r = Hero(name='Kamala Khan',super_name='Ms. Marvel')
            db.session.add(r)
            db.session.commit()
            assert hasattr(r, 'id')
            assert db.session.query(Hero).filter_by(id=r.id).first()

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


            assert db.session.query(Hero).filter_by(id=Khan.id).first().hero_powers == [h_p]