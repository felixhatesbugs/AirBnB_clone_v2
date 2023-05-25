#!/usr/bin/python3
"""starts a Flask web application
"""

from models import storage
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def return_n(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def return_n_template(n):
    """
    returns rendered html templates
    for number_template query
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def return_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.teardown_appcontext
def tear_session(self):
    """removes current SQLAlchemy Session
    after each session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def return_states():
    states = [v for v in storage.all("State").values()]
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
