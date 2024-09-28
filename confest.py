import pytest
from datetime import datetime


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    report_dir = "reports"
    now=datetime.now("%y-%m-%d-%d_%H-%M-%S")
    config.options.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("starting")
    yield
    print("End")





