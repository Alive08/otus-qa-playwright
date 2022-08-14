from multiprocessing.spawn import old_main_modules
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.elements.currency_dropdown import CurrencyDropdown


class MainPage(BasePage):

    def __init__(self, page: Page, url: str = '/'):
        super().__init__(page, url)
        self.currency_dropdown = CurrencyDropdown(self.page)

    @property
    def title(self):
        return "Your Store"

