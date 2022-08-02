import os
import sys

import pytest


def mydir():
    return os.path.dirname(os.path.abspath(__file__))


sys.path.append(mydir())


@pytest.fixture(scope='session')
def rootdir():
    return mydir()
