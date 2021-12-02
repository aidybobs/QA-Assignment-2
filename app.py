from flask import Flask, render_template, redirect
import requests
from os import getenv
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('databaseuri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')


db = SQLAlchemy(app)


class Character(db.Model):
    __tablename__ = 'Characters'
    char_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(20), nullable=False)
    archetype = db.Column(db.String(20), nullable=False)


arches = {
    'Two Handed Warrior': ['Heavy Armor', 'Two Handed'],
    'Battlemage': ['One Handed', 'Any magic tree', 'Enchanting'],
    'Hunter': ['Archery', 'Light Armor', 'Sneak'],
    'Warlock': ['Destruction', 'Conjuration', 'Enchanting', 'Light Armor'],
    'Paladin': ['Shield + One Handed/Two Handed', 'Restoration', 'Heavy Armor', 'Alteration'],
    'Assassin': ['One Handed(Dagger)', 'Sneak', 'Light Armor', 'Archery'],
    'Night Blade': ['One Handed(Dagger)', 'Illusion', 'Destruction', 'Sneak']
}


@app.route('/')
def generate():
    characters = db.Character.query.all()
    return render_template('home.html', characters=characters)


@app.route('/newchar', methods=['GET'])
def newchar():
    name = requests.get('http://name:5000/getname')
    race = requests.get('http://race:5000/getrace')
    archeno = requests.get('http://archetype:5000/getarche')
    arche = list(arches.keys())[archeno]
    char = Character(name=name, race=race, archetype=arche)
    db.session.add(char)
    db.session.commit()
    return redirect('/')
