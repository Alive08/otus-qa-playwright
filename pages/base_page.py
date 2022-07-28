from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page, url: str='/'):
        self.page = page
        self.url = url
    
    def open(self):
        self.page.goto(self.url)

    def __getattr__(self, attr):
        return getattr(self.page, attr)
