import pytest
from pages.store.main_page import MainPage
from playwright.sync_api import Page, expect


# @pytest.mark.skip
def test_fail(page: Page):
    page.goto('/')
    expect(page).not_to_have_title(MainPage(page).title)
