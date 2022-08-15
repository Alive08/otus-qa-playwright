import pytest
from pages.customer.main_page import MainPage
from playwright.sync_api import Page, expect


@pytest.mark.xfail(run=False)
def test_fail(page: Page):
    page.goto('/')
    expect(page).not_to_have_title(MainPage(page).title)
