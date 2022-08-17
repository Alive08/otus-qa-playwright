import allure
from playwright.sync_api import Page


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

    @allure.step("select currency {cur}")
    def select(self, cur):
        self.button.click()
        getattr(self, cur.lower()).click()
