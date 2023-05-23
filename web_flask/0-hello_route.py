#!/usr/bin/pyhton3
"""this script starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    returns hello world
    when root is queried
    """
    return 'Hello HBNB!'
