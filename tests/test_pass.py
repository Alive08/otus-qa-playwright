import pytest
from pages.customer.main_page import MainPage
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_pass(page: Page):
    page.goto('/')
    expect(page).to_have_title(MainPage(page).title)
