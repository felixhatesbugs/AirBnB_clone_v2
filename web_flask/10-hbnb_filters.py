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


@app.route('/states',  strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def return_states():
    """returns rendered html templates
    of states in database
    """
    states = [v for v in storage.all("State").values()]
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def return_state_cities():
    """returns rendered html templates
    of cities by state in database
    """
    states = [v for v in storage.all("State").values()]
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def return_states_id(id):
    state = None
    for v in storage.all('State').values():
        if v.id == id:
            state = v
            break
    return render_template('9-states.html', state=state)


@app.route('/hbnb_filters', strict_slashes=False)
def return_hbnb_filters():
    states = [v for v in storage.all("State").values()]
    amenities = [v for v in storage.all("Amenity").values()]
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
