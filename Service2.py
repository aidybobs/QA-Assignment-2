from nameraceparse import races
from flask import Flask, Response
from random import choice

app = Flask(__name__)


@app.route('/getrace', methods=['GET'])
def getrace():
    return Response(choice(races), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
