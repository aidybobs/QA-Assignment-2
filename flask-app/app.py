from flask import Flask, render_template, redirect, request
from os import getenv
import requests
from random import choice
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skyrim.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'djhsadsa'


db = SQLAlchemy(app)


class Character(db.Model):
    __tablename__ = 'Characters'
    char_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(20), nullable=False)
    archetype = db.Column(db.String(20), nullable=False)


@app.route('/')
def generate():
    characters = Character.query.all()
    return render_template('home.html', characters=characters)


@app.route('/newchar', methods=['GET'])
def newchar():
    if request.method == 'GET':
        character = requests.post('http://character:5000/getchar')
        character_json = character.json()
        name = choice(character_json['name'])
        char = Character(name=name, race=character_json['race'], archetype=character_json['arche'])
        db.session.add(char)
        db.session.commit()
        return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
