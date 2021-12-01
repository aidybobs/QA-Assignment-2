from flask import Flask, Response
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate():
