from ast import dump
from flask import Flask, jsonify
from database import Session, engine
from models import User

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def users():
    return "hola"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
