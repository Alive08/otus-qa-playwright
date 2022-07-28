from playwright.sync_api import Page, expect
from pages.store.main_page import MainPage


def test_at_main_page(page: Page):
    p = MainPage(page=page)
    p.open()
    assert p.title() == 'Your Store'


