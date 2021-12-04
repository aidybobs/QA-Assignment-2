from flask import Response
from random import randint
from application import app


@app.route('/getarche', methods=['GET'])
def getarche():
    return Response(str(randint(0, 6)), mimetype='text/plain')
