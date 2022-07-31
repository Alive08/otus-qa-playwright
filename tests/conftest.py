import pytest
from frame.classes import Creds
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
