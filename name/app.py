from flask import Flask, Response
from random import choice
import pandas as pd
import requests
app = Flask(__name__)

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
    return Response(choice(archenames.values.tolist()), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
