"""
    self = (By.CSS_SELECTOR, "a[title='My Account']")
    login = (By.LINK_TEXT, "Login")
    register = (By.LINK_TEXT, "Register")
    my_account = (By.LINK_TEXT, "My Account")
    order_history = (By.LINK_TEXT, "Order History")
    transactions = (By.LINK_TEXT, "Transactions")
    downloads = (By.LINK_TEXT, "Downloads")
    logout = (By.LINK_TEXT, "Logout")
"""
from playwright.sync_api import Page

class AccountDropdown:

    def __init__(self, page: Page):
        self.page = page

    @property
    def menu(self):
        return self.page.locator("a[title='My Account']")

    @property
    def login(self):
        return self.page.locator("#top-links >> text=Login")

    @property
    def register(self):
        return self.page.locator("#top-links >> text=Register")

    @property
    def my_account(self):
        return self.page.locator('a', has_text='My Account')
        
    @property
    def logout(self):
        return self.page.locator("#top-links >> text=Logout")
