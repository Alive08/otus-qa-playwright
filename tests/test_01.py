from playwright.sync_api import Page, expect


def test_01(page: Page):
    page.goto("/")
