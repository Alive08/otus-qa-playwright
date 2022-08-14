import allure
from frame.logger import _init_logger
from playwright.sync_api import Locator, Page


class BasePage:

    def __init__(self, page: Page, url: str = '/'):
        self.page = page
        self.url = url
        self._logger = _init_logger(type(self).__name__)

    @allure.step("open page")
    def open(self):
        self._logger.info("navigate to %s", self.url)
        self.page.goto(self.url)

    def __getattr__(self, attr):
        return getattr(self.page, attr)

    @allure.step("input text {text} with dropdown in {locator}")
    def fill_with_dropdown(self, locator: Locator, text: str):
        self._logger.info(
            "input text with dropdown %s in %s", text, locator)

        with allure.step(f"input text {text} in {locator}"):
            locator.fill(text)

        with allure.step("click on dropdown"):
            try:
                self.locator(".dropdown-menu >> a", has_text=text).click()
            except:
                locator.fill(value='')

        return locator
