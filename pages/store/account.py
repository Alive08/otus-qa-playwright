import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.elements.account_dropdown import AccountDropdown


class CustomerAccount(BasePage):

    """
        LOCATOR_BUTTON_CONTINUE = Selector(
            By.CSS_SELECTOR, '#content > div > div > a')
        LOCATOR_INPUT_EMAIL = Selector(By.ID, 'input-email')
        LOCATOR_INPUT_PASSWORD = Selector(By.ID, 'input-password')
        LOCATOR_BUTTON_LOGIN = Selector(By.CSS_SELECTOR, 'input[type=submit]')

    """

    def __init__(self, page: Page, url: str = '/index.php?route=account/login'):
        super().__init__(page, url)
        self.account_dropdown = AccountDropdown(self.page)

    @property
    def login_title(self):
        return "Account Login"

    @property
    def logout_title(self):
        return "Account Logout"

    @property
    def account_title(self):
        return "My Account"

    @property
    def forgotten_password_title(self):
        return "Forgot Your Password?"

    @property
    def email_input(self):
        return self.page.locator("#input-email")

    @property
    def password_input(self):
        return self.page.locator("#input-password")

    @property
    def login_button(self):
        # for demo purpose
        # return self.page.locator("text='Login'")
        return self.page.locator("input:has-text('Login')")

    @property
    def forgotten_password_back_button(self):
        return self.page.locator("a.btn.btn-default")

    @property
    def forgotten_password_continue_button(self):
        return self.page.locator("button.btn.btn-primary")

    @property
    def forgotten_password_link(self):
        return self.page.locator("text='Forgotten Password'")

    @property
    def alert_success_message(self):
        return self.page.locator("div.alert.alert-success.alert-dismissible")

    @property
    def alert_danger_message(self):
        return self.page.locator("div.alert.alert-danger.alert-dismissible")

    @property
    def close_alert_button(self):
        return self.page.locator("button.close")

    @allure.step("open the page")
    def open(self):
        self._logger.info("navigate to %s", self.url)
        self.page.goto(self.url)

    @allure.step("do login with {email} / {password}")
    def login_with(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("do logout")
    def logout(self):
        self.account_dropdown.menu.click()
        self.account_dropdown.logout.click()
