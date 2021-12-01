from flask import Flask, Response
from random import choice
import csv

app = Flask(__name__)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    races = next(csv_reader)

@app.route('/getrace', methods=['GET'])
def getrace():
    return Response(choice(races), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
