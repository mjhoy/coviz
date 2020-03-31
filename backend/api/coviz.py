"""Interacting with external COVIZ data."""
import pkg_resources

import pandas as pd


def read_confirmed_time_series():
    """Read latest new confirmed by day csv."""
    return pd.read_csv(
        pkg_resources.resource_stream(
            "api",
            "COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
            "time_series_covid19_confirmed_global.csv",
        )
    )
