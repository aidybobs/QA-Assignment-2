from flask import Flask, Response
from random import choice
import pandas as pd
import requests
app = Flask(__name__)

arche = {
    'Two Handed Warrior': ['Heavy Armor', 'Two Handed'],
    'Battlemage': ['One Handed', 'Any magic tree', 'Enchanting'],
    'Hunter': ['Archery', 'Light Armor', 'Sneak'],
    'Warlock': ['Destruction', 'Conjuration', 'Enchanting', 'Light Armor'],
    'Paladin': ['Shield + One Handed/Two Handed', 'Restoration', 'Heavy Armor', 'Alteration'],
    'Assassin': ['One Handed(Dagger)', 'Sneak', 'Light Armor', 'Archery'],
    'Night Blade': ['One Handed(Dagger)', 'Illusion', 'Destruction', 'Sneak']
}

data = pd.read_csv('../names.csv')




@app.route('/getname)', methods=['POST'])
def getname():
    race = requests.get('http://race:5000/getrace')
    archetype = requests.get('http://archetype:5000/getarche')
    racenames = pd.DataFrame(data=data.loc[:, race])
    archenames = pd.DataFrame()
    for index, row in racenames.iterrows():
        if index % 7 == archetype:
            archenames.append(index, row[race])
