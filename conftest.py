import os
import sys

import pytest

pytest_plugins = [
    "fixtures.data",
    "fixtures.db",
    "fixtures.logger",
    "fixtures.pages"
]


def mydir():
    return os.path.dirname(os.path.abspath(__file__))


sys.path.append(mydir())


@pytest.fixture(scope='session')
def rootdir():
    return mydir()
