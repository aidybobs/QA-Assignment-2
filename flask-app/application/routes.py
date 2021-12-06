from application import app, db
from flask import request, redirect, render_template
from random import choice
from application.models import Characters
import requests


@app.route('/')
def generate():
    characters = Characters.query.all()
    return render_template('home.html', characters=characters)


@app.route('/newchar', methods=['GET'])
def newchar():
    if request.method == 'GET':
        character = requests.post('http://character:5000/getchar')
        character_json = character.json()
        name = choice(character_json['name'])
        char = Characters(name=name, race=character_json['race'], archetype=character_json['arche'])
        db.session.add(char)
        db.session.commit()
        return redirect('/')
