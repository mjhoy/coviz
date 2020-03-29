"""App tools and routing for the backend."""
from flask import Flask

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route("/covid/confirmed/new/<date>")
def get_new_confirmed(date):
    """Get new confirmed COVID-19 cases on date."""
    return f"new on {date}"


@app.route("/covid/confirmed/total/<date>")
def get_confirmed_to_date(date):
    """Get total number of COVID-19 cases to date."""
    return f"total up to {date}"
