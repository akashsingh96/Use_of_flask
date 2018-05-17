#!flask/bin/python
from flask import Flask

wed1 = Flask(__name__)

@wed1.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    wed1.run(debug=True)
