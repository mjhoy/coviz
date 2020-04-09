import datetime
import pandas as pd

from api import coviz


def test_read_confirmed_time_series():
    index = ["Province/State", "Country/Region"]
    non_date_columns = ["Lat", "Long"]
    date_columns = list(
        pd.date_range(start="2020-01-22", end="2020-04-03").strftime("%-m/%-d/%-y")
    )
    columns = non_date_columns + date_columns

    actual = coviz.read_confirmed_time_series()

    assert isinstance(actual, pd.DataFrame)
    assert (
        set(columns) - set(actual.columns) == set()
    ), "Try running `git submodule update` and then re-running tests"
    assert set(index) - set(actual.index.names) == set()
