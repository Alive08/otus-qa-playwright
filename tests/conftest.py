import time
from pathlib import Path
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from frame.classes import Creds
from frame.logger import _init_logger
from pages.admin.login_page import AdminLogin
from playwright.sync_api import Page, expect


def pytest_addoption(parser):
    parser.addoption("--myip", default='localhost')
    parser.addoption("--db-host", default='localhost')
    parser.addoption("--bversion", default=None)
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


@pytest.fixture(scope='session')
def account_admin_valid():
    return Creds('user', 'bitnami')


@pytest.fixture(scope='session')
def account_admin_invalid():
    return Creds('user', 'bitn@mi')


@pytest.fixture()
def admin_login_page(page: Page):
    login_page = AdminLogin(page=page, url='/admin')
    login_page.open()
    expect(login_page.page).to_have_title(login_page.login_title)
    return login_page


# https://docs.pytest.org/en/latest/example/simple.html#post-process-test-reports-failures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield

    rep = outcome.get_result()

    # set a report attribute for each phase of a call
    # which can be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


def take_screenshot_playwright(page: Page, dir, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/",
                                                                                      "_").replace("::", "__")

    with open(f"{dir}/{file_name}", 'wb') as bin_file:
        bin_file.write(page.screenshot(full_page=True))

    return file_name


def take_screenshot_allure(page: Page, nodeid):
    # time.sleep(1)
    allure.attach(page.screenshot(full_page=True, type='png'), name=nodeid,
                  attachment_type=AttachmentType.PNG)


@pytest.fixture(scope="function", autouse=True)
def fail_check(request, page, _logger, screenshots_dir):

    yield

    if request.node.rep_setup.failed:
        _logger.error("setting up a test %s failed", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            # driver = request.node.funcargs['driver']
            screenshot = take_screenshot_playwright(
                page, screenshots_dir, request.node.nodeid)
            take_screenshot_allure(page, request.node.nodeid)
            _logger.error("executing test %s failed", request.node.nodeid)
            _logger.info("screenshot saved in %s",
                         Path(screenshots_dir, screenshot))
