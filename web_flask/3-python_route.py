#!/usr/bin/python3
"""adds /c route to the server
that takes a variable <text>"""

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


@app.route('/c/<text>', strict_slashes=False)
def return_c(text):
    """
    returns : “C ” followed by the value of the text
    syntax  : /c/<text>
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def return_python(text="is_cool"):
    """
    returns : “Python ”, followed by the value of the text"
    syntax  : /python/(<text>)
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
