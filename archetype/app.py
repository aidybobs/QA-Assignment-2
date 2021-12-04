from flask import Flask, Response
from random import randint
app = Flask(__name__)


@app.route('/getarche', methods=['GET'])
def getarche():
    return Response(str(randint(0, 6)), mimetype='text/plain')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
