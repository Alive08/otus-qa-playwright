from playwright.sync_api import Page
from frame.logger import _init_logger


class BasePage:

    def __init__(self, page: Page, url: str='/'):
        self.page = page
        self.url = url
        self._logger = _init_logger(type(self).__name__)
    
    def open(self):
        self.page.goto(self.url)

    def __getattr__(self, attr):
        return getattr(self.page, attr)
