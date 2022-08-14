import pytest
from playwright.sync_api import Page, expect

from pages.admin.account import AdminAccount
from pages.customer.account import CustomerAccount
from pages.customer.main_page import MainPage


@pytest.fixture()
def admin_page(page: Page):
    _page = AdminAccount(page=page, url='/admin')
    _page.open()
    expect(_page.page).to_have_title(_page.login_title)
    return _page


@pytest.fixture()
def customer_page(page: Page):
    _page = CustomerAccount(page=page, url='/index.php?route=account/login')
    _page.open()
    expect(_page.page).to_have_title(_page.login_title)
    return _page


@pytest.fixture()
def main_page(page: Page):
    _page = MainPage(page=page, url='/')
    _page.open()
    expect(_page.page).to_have_title(_page.title)
    return _page
