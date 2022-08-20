import pytest


def pytest_addoption(parser):
    parser.addoption("--myip", default='localhost')
    parser.addoption("--db-host", default='localhost')
    parser.addoption("--test-log-level", default="INFO",
                     choices=("DEBUG", "INFO", "WARNING", "ERROR"))
    parser.addoption("--test-log-file", default="artifacts/testrun.log")
    parser.addoption("--screenshots-dir", default="artifacts/screenshots")


def pytest_configure(config: pytest.Config):
    global option
    option = config.option


@pytest.fixture(scope='session')
def options():
    return option


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        # "proxy": {
        #     "server": "http://opencart:3128"
        # }
    }


@pytest.fixture(scope='session')
def my_IP(request):
    return request.config.getoption("--myip")


@pytest.fixture(scope='session')
def db_host(request):
    return request.config.getoption("--db-host")
