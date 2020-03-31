import pkg_resources


def test_covid_confirmed_time_series_global():
    print(pkg_resources.resource_listdir("api", "COVID-19"))
    assert pkg_resources.resource_exists(
        "api",
        "COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
        "time_series_covid19_confirmed_global.csv",
    ), "Try `git submodule update` and then re-run tests"
