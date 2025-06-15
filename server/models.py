from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-hero_powers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='hero',cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Hero {self.id}, {self.name} {self.super_name}>'

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_rules = ('-hero_powers.power',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='power',cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Power {self.id}, {self.name} {self.description}>'

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    serialize_rules = ('-hero.hero_powers','-power.hero_powers')

    id = db.Column(db.Integer, primary_key=True)
    _strength = db.Column('strength',db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    def __repr__(self):
        return f'<HeroPower {self.id}, {self.strength}>'
    
    @property
    def strength(self):
        return self._strength
    
    @strength.setter    
    def strength(self, value):
        allowed = ['Strong', 'Weak', 'Average']
        if value not in allowed:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")
        self._strength = value