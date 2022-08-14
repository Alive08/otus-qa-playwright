from dataclasses import dataclass

import allure
from pages.base_page import BasePage
from pages.elements.account_dropdown import AccountDropdown
from playwright.sync_api import Page


@dataclass
class AccountErrors:

    TEXT_ACCOUNT_CREATED = "Your Account Has Been Created!"
    TEXT_PASSWORDS_MISMATCH = "Password confirmation does not match password!"
    TEXT_FIRST_NAME_ERROR = "First Name must be between 1 and 32 characters!"
    TEXT_LAST_NAME_ERROR = "Last Name must be between 1 and 32 characters!"
    TEXT_EMAIL_ERROR = "E-Mail Address does not appear to be valid!"
    TEXT_TELEPHONE_ERROR = "Telephone must be between 3 and 32 characters!"
    TEXT_PASSWORD_ERROR = "Password must be between 4 and 20 characters!"


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
        return self.page.locator("text=Back")

    @property
    def forgotten_password_continue_button(self):
        return self.page.locator("text=Continue")

    @property
    def forgotten_password_link(self):
        return self.page.locator("#content >> text=Forgotten Password")

    @property
    def new_account_continue_button(self):
        return self.page.locator("a", has_text='Continue')

    @property
    def new_account_input_firstname(self):
        return self.page.locator("#input-firstname")

    @property
    def new_account_input_lastname(self):
        return self.page.locator("#input-lastname")

    @property
    def new_account_input_email(self):
        return self.page.locator("#input-email")

    @property
    def new_account_input_telephone(self):
        return self.page.locator("#input-telephone")

    @property
    def new_account_input_password_1(self):
        return self.page.locator("#input-password")

    @property
    def new_account_input_password_2(self):
        return self.page.locator("#input-confirm")

    @property
    def privacy_policy_link(self):
        return self.page.locator("#content > form > div > div > a")

    @property
    def privacy_policy_box(self):
        return self.page.locator("input[type=checkbox]")

    @property
    def new_account_submit(self):
        return self.page.locator("input:has-text('Continue')")

    @property
    def alert_success_message(self):
        return self.page.locator("div.alert.alert-success.alert-dismissible")

    @property
    def alert_danger_message(self):
        return self.page.locator("div.alert.alert-danger.alert-dismissible")

    @property
    def close_alert_button(self):
        return self.page.locator("button.close")

    @property
    def text_danger(self):
        return self.page.locator("div.text-danger")

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

    @allure.step("submit password restore form for {email}")
    def restore_password(self, email):
        self.email_input.fill(email)
        self.forgotten_password_continue_button.click()

    @allure.step("fill in and submit registration form")
    def register_account(self, data, agree=True):
        self._logger.info("fill in and submit registration form")
        self.new_account_input_firstname.fill(data.fname)
        self.new_account_input_lastname.fill(data.lname)
        self.new_account_input_email.fill(data.email)
        self.new_account_input_telephone.fill(data.phone)
        self.new_account_input_password_1.fill(data.password_1)
        self.new_account_input_password_2.fill(data.password_2)
        if agree:
            self.privacy_policy_box.check()
        self.new_account_submit.click()
