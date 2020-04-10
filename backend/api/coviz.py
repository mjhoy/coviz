"""Interacting with external COVIZ data."""
import logging
import pkg_resources

import pandas as pd

_logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


def read_confirmed_time_series():
    """Read latest new confirmed by day csv."""
    _logger.info("Reading time series data...")
    return pd.read_csv(
        pkg_resources.resource_stream(
            "api",
            "COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
            "time_series_covid19_confirmed_global.csv",
        ),
        index_col=["Country/Region", "Province/State"],
    )
