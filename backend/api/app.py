"""App tools and routing for the backend."""
import logging

from flask import Flask

from .coviz import read_confirmed_time_series

app = Flask(__name__)  # pylint: disable=invalid-name
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


@app.route("/")
def health_check():
    """Ping test."""
    _logger.info("Ping! health check...")
    return "Success"


@app.route("/covid/confirmed/new/<date>")
def get_new_confirmed(date):
    """Get new confirmed COVID-19 cases on date."""
    _logger.info("Getting new confirmed COVID-19 cases for %s", date)
    return read_confirmed_time_series().to_json()


@app.route("/covid/confirmed/total/<date>")
def get_confirmed_to_date(date):
    """Get total number of COVID-19 cases to date."""
    _logger.info("Getting total confirmed COVID-19 cases by %s", date)
    return read_confirmed_time_series().to_json()
