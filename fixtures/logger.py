from pathlib import Path

import pytest
from frame.logger import _init_logger
from frame.utils import Utils


@pytest.fixture(scope='session')
def _app_logger(options):
    return _init_logger('', level=options.test_log_level, logfile=options.test_log_file)


# logger for conftest's fixtures
@pytest.fixture(scope='session')
def _logger(options, _app_logger):
    return _init_logger(__name__)


@pytest.fixture(autouse=True)
def log(request, _logger):
    _logger.info(">>> RUN <%s> <<<", request.node.name)

    yield

    _logger.info(">>> END <%s> <<<", request.node.name)


@pytest.fixture(scope='session')
def screenshots_dir(rootdir, _logger):
    workdir = Path(rootdir, "artifacts/screenshots")
    try:
        workdir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        _logger.exception(e)
        pytest.fail()
    else:
        _logger.info("created screenshots directory %s", workdir)
        return workdir


# https://docs.pytest.org/en/latest/example/simple.html#post-process-test-reports-failures


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield

    rep = outcome.get_result()

    # set a report attribute for each phase of a call
    # which can be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def fail_check(request, page, _logger, screenshots_dir):

    yield

    if request.node.rep_setup.failed:
        _logger.error("setting up a test %s failed", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            # driver = request.node.funcargs['driver']
            screenshot = Utils.take_screenshot_playwright(
                page, screenshots_dir, request.node.nodeid)
            Utils.take_screenshot_allure(page, request.node.nodeid)
            _logger.error("executing test %s failed", request.node.nodeid)
            _logger.info("screenshot saved in %s",
                         Path(screenshots_dir, screenshot))
