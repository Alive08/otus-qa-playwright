from pages.base_page import BasePage
from pages.elements.currency_dropdown import CurrencyDropdown
from playwright.sync_api import Page


class MainPage(BasePage):

    def __init__(self, page: Page, url: str = '/'):
        super().__init__(page, url)
        self.currency_dropdown = CurrencyDropdown(self.page)

    @property
    def title(self):
        return "Your Store"
