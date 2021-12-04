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


@app.route('/')
def generate():
    characters = db.Character.query.all()
    return render_template('home.html', characters=characters)


@app.route('/newchar', methods=['GET'])
def newchar():
    character = requests.get('http://character:5000/getchar')
    character_json = character.json()
    char = Character(name=character_json['name'], race=character_json['race'], archetype=character_json['arche'])
    db.session.add(char)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
