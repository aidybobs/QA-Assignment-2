from nameraceparse import races
from flask import Flask, Response
from random import randint

app = Flask(__name__)


@app.route('/generaterace', methods=['GET'])
def getrace():
    return Response(races[randint(0, 9)], mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
