from flask import Flask, jsonify
import pandas as pd
import requests


app = Flask(__name__)


data = pd.read_csv('resources/names.csv')


arches = {
    'Two Handed Warrior': ['Heavy Armor', 'Two Handed'],
    'Battlemage': ['One Handed', 'Any magic tree', 'Enchanting'],
    'Hunter': ['Archery', 'Light Armor', 'Sneak'],
    'Warlock': ['Destruction', 'Conjuration', 'Enchanting', 'Light Armor'],
    'Paladin': ['Shield + One Handed/Two Handed', 'Restoration', 'Heavy Armor', 'Alteration'],
    'Assassin': ['One Handed(Dagger)', 'Sneak', 'Light Armor', 'Archery'],
    'Night Blade': ['One Handed(Dagger)', 'Illusion', 'Destruction', 'Sneak']
}


@app.route('/getname)', methods=['POST'])
def getname():
    race = requests.get('http://race:5000/getrace')
    archetype = requests.get('http://archetype:5000/getarche')
    racenames = data[race.text].tolist()
    archenames = []
    arche = list(arches.keys())[int(archetype.text)]
    i = 0
    while i <= 19:
        if i % 7 == int(archetype.text):
            archenames.append(racenames[i])
            i += 1
        else:
            i += 1

    return jsonify({
        'name': archenames,
        'race': race.text,
        'arche': arche
    })


if __name__ == '__main__':
    app.run(port=5003, host='0.0.0.0')