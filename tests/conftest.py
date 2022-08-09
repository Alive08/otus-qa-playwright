import json
import logging
import random
import time
from datetime import datetime
from pathlib import Path

import pytest
from faker import Faker
from frame.classes import AccountData, Creds, ProductData
from frame.db import DB
from frame.logger import _init_logger
from frame.utils import Utils
from pages.admin.login_page import AdminLogin
from pages.elements.account_dropdown import AccountDropdown
from pages.elements.currency_dropdown import CurrencyDropdown
from pages.store.login_page import CustomerLogin
from pages.store.main_page import MainPage
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
def my_IP(request):
    return request.config.getoption("--myip")


@pytest.fixture(scope='session')
def db_host(request):
    return request.config.getoption("--db-host")


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


@pytest.fixture
def account_valid():
    return AccountData(
        fname='Denzel',
        lname='Washington',
        email='denzel.washington@holliwood.com',
        phone='1 234 5678 90',
        password_1='helloUser',
        password_2='helloUser',
    )


@pytest.fixture
def account_random():
    faker = Faker()
    return AccountData(
        fname=faker.first_name(),
        lname=faker.last_name(),
        email=faker.email(),
        phone=faker.phone_number(),
        password_1=faker.password(),
        password_2=faker.password(),
    )


@pytest.fixture
def product_random():
    faker = Faker()
    return ProductData(
        name=f'test_{faker.word()}',
        description=faker.paragraph(),
        model=f'test_{faker.word()}',
        price=faker.pyint(),
        quantity=faker.pyint(),
        # categories=random.choice(product.item_names)
    )


@pytest.fixture(scope='session')
def db_connector(db_host):
    connection = DB(host=db_host, database='bitnami_opencart',
                    user='bn_opencart', password='')

    yield connection

    connection.close()


@pytest.fixture
def db_product_random(db_connector: DB, product_random, _logger):
    _logger.info("adding random product")

    yield db_connector.add_product(product_random)

    _logger.info("deleting product")
    db_connector.delete_product('test')


@pytest.fixture
def db_delete_product(db_connector: DB, _logger):

    yield

    _logger.info("deleting product")
    db_connector.delete_product('test')


@pytest.fixture
def db_customer_valid(db_connector: DB, account_valid, _logger):
    _logger.info("adding valid customer account")

    yield db_connector.create_customer(account_valid)

    _logger.info("deleting customer {}".format(account_valid.email))
    db_connector.delete_customer(account_valid.email)


@pytest.fixture
def db_delete_customer_valid(db_connector: DB, account_valid, _logger):
    _logger.info("deleting valid customer account")

    yield

    _logger.info("deleting customer {}".format(account_valid.email))
    db_connector.delete_customer(account_valid.email)


@pytest.fixture
def db_customer_random(db_connector: DB, account_random, _logger):
    _logger.info("adding random customer account")

    yield db_connector.create_customer(account_random)

    _logger.info("deleting customer {}".format(account_random.email))
    db_connector.delete_customer(account_random.email)


@pytest.fixture
def db_delete_customer_random(db_connector: DB, account_random, _logger):
    _logger.info("deleting random customer account")

    yield

    _logger.info("deleting customer {}".format(account_random.email))
    db_connector.delete_customer(account_random.email)

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

# Pages fixtures


@pytest.fixture()
def admin_login_page(page: Page):
    login_page = AdminLogin(page=page, url='/admin')
    login_page.open()
    expect(login_page.page).to_have_title(login_page.login_title)
    return login_page


@pytest.fixture()
def customer_login_page(page: Page):
    login_page = CustomerLogin(page=page, url='/index.php?route=account/login')
    login_page.account_dropdown = AccountDropdown(page)
    login_page.open()
    expect(login_page.page).to_have_title(login_page.login_title)
    return login_page


@pytest.fixture()
def main_page(page: Page):
    main_page = MainPage(page=page, url='/')
    main_page.currency = CurrencyDropdown(page)
    main_page.open()
    expect(main_page.page).to_have_title(main_page.title)
    return main_page
