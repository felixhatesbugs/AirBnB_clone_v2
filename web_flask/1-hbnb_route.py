#!/usr/bin/python3
"""adds /hbnb route to the server"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def return_hello():
    """
    returns hello world
    when root is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def return_hbnb():
    """
    returns page for
    /hbnb route query
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
