import pytest
from frame.classes import Creds
from pages.admin.login_page import AdminLoginPage
from playwright.sync_api import expect, Page


@pytest.fixture(scope='session')
def account_admin_valid():
    return Creds('user', 'bitnami')


@pytest.fixture(scope='session')
def account_admin_invalid():
    return Creds('user', 'bitn@mi')


@pytest.fixture()
def login_page(page: Page):
    login_page = AdminLoginPage(page=page, url='/admin')
    login_page.open()
    expect(login_page.page).to_have_title(login_page.login_title)
    return login_page
