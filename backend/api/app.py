"""App tools and routing for the backend."""
from flask import Flask

from .coviz import read_confirmed_time_series

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route("/")
def health_check():
    """Ping test."""
    return "Success"


@app.route("/covid/confirmed/new/<date>")
def get_new_confirmed(date):
    """Get new confirmed COVID-19 cases on date."""
    print(date)
    return read_confirmed_time_series().to_json()


@app.route("/covid/confirmed/total/<date>")
def get_confirmed_to_date(date):
    """Get total number of COVID-19 cases to date."""
    print(date)
    return read_confirmed_time_series().to_json()
