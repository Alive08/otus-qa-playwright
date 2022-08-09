
"""
    form = (By.CSS_SELECTOR, "#form-currency")
    button = (By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle")
    self = (By.CSS_SELECTOR, "ul.dropdown-menu")
    usd = (By.CSS_SELECTOR, "button[name=USD]")
    eur = (By.CSS_SELECTOR, "button[name=EUR]")
    gbp = (By.CSS_SELECTOR, "button[name=GBP]")
    selected = (By.CSS_SELECTOR, "strong")
"""
from playwright.sync_api import Page
from frame.classes import Currency


class CurrencyDropdown:

    def __init__(self, page: Page):
        self.page = page

    @property
    def form(self):
        return self.page.locator("#form-currency")

    @property
    def button(self):
        return self.page.locator("button.btn.btn-link.dropdown-toggle")

    @property
    def menu(self):
        return self.page.locator("ul.dropdown-menu")

    @property
    def usd(self):
        return self.page.locator("button[name=USD]")

    @property
    def eur(self):
        return self.page.locator("button[name=EUR]")

    @property
    def gbp(self):
        return self.page.locator("button[name=GBP]")

    @property
    def selected(self):
        return self.page.locator("strong")

    def select(self, cur):
        self.button.click()
        getattr(self, cur.lower()).click()
