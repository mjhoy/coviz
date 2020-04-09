"""App tools and routing for the backend."""
import datetime
import logging

from flask import Flask
import pandas as pd

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
    """Get new confirmed COVID-19 cases to date."""
    _logger.info("Getting new confirmed COVID-19 cases for %s")

    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    time_series = read_confirmed_time_series()

    data = time_series[date.strftime("%-m/%-d/%-y")].groupby(level="Country/Region").sum()
    return data.to_json()


@app.route("/covid/confirmed/total/<date>")
def get_confirmed_to_date(date):
    """Get total number of COVID-19 cases to date."""
    _logger.info("Getting total confirmed COVID-19 cases by %s", date)
    start_date = datetime.datetime(2020, 1, 22)
    end_date = datetime.datetime.strptime(date, "%Y-%m-%d")

    time_series = read_confirmed_time_series().drop(columns=["Lat", "Long"])
    date_range = pd.date_range(start_date, end_date).strftime("%-m/%-d/%-y")
    date_range = set(date_range).intersection(set(time_series.columns))

    data = time_series[date_range].groupby(level="Country/Region").sum().sum(axis=1)
    return data.to_json()
