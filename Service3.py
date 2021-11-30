from flask import Flask, Response
from random import choice
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


@app.route('/getarche', methods=['GET'])
def getarche():
    arches = list(arche.keys())
    return Response(choice(arches), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
