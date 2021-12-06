from flask import Response
from random import choice
from application import app


@app.route('/getrace', methods=['GET'])
def getrace():
    races = ['High Elf', 'Argonian', 'Wood Elf', 'Breton', 'Dark Elf', 'Imperial', 'Khajiit', 'Nord', 'Orc', 'Redguard']
    return Response(choice(races), mimetype='text/plain')
