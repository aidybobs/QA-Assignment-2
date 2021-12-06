from application import app
from flask import Response
from random import randint


@app.route('/getarche', methods=['GET'])
def getarche():
    return Response(str(randint(0, 6)), mimetype='text/plain')