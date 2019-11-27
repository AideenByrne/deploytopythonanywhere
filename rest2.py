#Aideen Byrne Big Project
#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__, static_url_path='', static_folder='.')

app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)