import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now=datetime.now.strftime("%y-%m-%d-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("starting")
    yield
    print("End")





