# server/app.py
#!/usr/bin/env python3
from flask import Flask, make_response, request
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return make_response('Oh yes, It is about Superheroes',200)

@app.route('/heroes')
def heroes():
    heroes = Hero.query.all()
    return make_response([{"id": hero.id, "name": hero.name,"super_name": hero.super_name,} for hero in heroes],200)

@app.route('/heroes/<int:id>')
def heroById(id):
    hero = Hero.query.filter_by(id=id).first()
    if hero:
        return make_response(hero.to_dict(),200)
    else:
        return make_response({"error": "Hero not found"},404)
    
@app.route('/powers')
def powers():
    powers = Power.query.all()
    return make_response([{"id": power.id, "description": power.description,"name": power.name,} for power in powers],200)

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def powerById(id):
    power = Power.query.filter_by(id=id).first()
    if not power:
        return make_response({"error": "Power not found"}, 404)

    if request.method == 'GET':
        return make_response(power.to_dict(), 200)
    
    elif request.method == 'PATCH':
        try:
            data = request.get_json()
            for attr in data:
                setattr(power, attr, data[attr])

            db.session.add(power)
            db.session.commit()
            return make_response(power.to_dict(), 200)

        except ValueError as e:
            return make_response({"errors": [str(e)]}, 400)
        
@app.route('/hero_powers',methods=['POST'])
def hero_powers():
    try:
        data = request.get_json()
        new_hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(new_hero_power)
        db.session.commit()

        return make_response(new_hero_power.to_dict(),200)
    except ValueError as e:
        return make_response({"errors": ["validation errors"]}, 400)



if __name__ == '__main__':
    app.run(port=5555, debug=True)