import datetime
import pandas as pd

from api import coviz


def test_read_confirmed_time_series():
    non_date_columns = ["Province/State", "Country/Region", "Lat", "Long"]
    date_columns = list(
        pd.date_range(
            start="2020-01-22", end=datetime.date.today() - datetime.timedelta(days=2)
        ).strftime("%-m/%-d/%-y")
    )
    columns = non_date_columns + date_columns

    actual = coviz.read_confirmed_time_series()

    assert isinstance(actual, pd.DataFrame)
    assert (
        set(columns) - set(actual.columns) == set()
    ), "Try running `git submodule update` and then re-running tests"
