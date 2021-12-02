from flask import Flask, Response, jsonify
from random import choice
import pandas as pd
import requests
app = Flask(__name__)

data = pd.read_csv('../names.csv')


arches = {
    'Two Handed Warrior': ['Heavy Armor', 'Two Handed'],
    'Battlemage': ['One Handed', 'Any magic tree', 'Enchanting'],
    'Hunter': ['Archery', 'Light Armor', 'Sneak'],
    'Warlock': ['Destruction', 'Conjuration', 'Enchanting', 'Light Armor'],
    'Paladin': ['Shield + One Handed/Two Handed', 'Restoration', 'Heavy Armor', 'Alteration'],
    'Assassin': ['One Handed(Dagger)', 'Sneak', 'Light Armor', 'Archery'],
    'Night Blade': ['One Handed(Dagger)', 'Illusion', 'Destruction', 'Sneak']
}


@app.route('/getname)', methods=['GET'])
def getname():
    race = requests.get('http://race:5000/getrace')
    archetype = requests.get('http://archetype:5000/getarche')
    racenames = pd.DataFrame(data=data.loc[:, race])
    archenames = pd.DataFrame()
    arche = list(arches.keys())[archetype]
    for index, row in racenames.iterrows():
        if index % 7 == archetype:
            archenames.append(index, row[race])
    return jsonify({
        'character': choice(archenames.values.tolist()),
        'race': race,
        'arche': arche
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
