from pages.base_page import BasePage
'''

    URL = '/admin'

    URL_ADMIN_LOGIN_PAGE = URL

    TITLE_ADMIN_LOGIN_PAGE = "Administration"
    TITLE_ADMIN_PAGE = "Dashboard"
    TITLE_FORGOTTEN_PASSWORD_PAGE = "Forgot Your Password?"

    LOCATOR_INPUT_USERNAME = Selector(By.CSS_SELECTOR, "#input-username")
    LOCATOR_INPUT_PASSWORD = Selector(By.CSS_SELECTOR, "#input-password")
    LOCATOR_INPUT_EMAIL = Selector(By.CSS_SELECTOR, "#input-email")

    LOCATOR_BUTTON_LOGIN_SUBMIT = Selector(
        By.CSS_SELECTOR, "button.btn.btn-primary")
    LOCATOR_BUTTON_FORGOTTEN_PASSWORD_CANCEL = Selector(
        By.CSS_SELECTOR, "a.btn.btn-default")
    LOCATOR_BUTTON_FORGOTTEN_PASSWORD_SUBMIT = Selector(
        By.CSS_SELECTOR, "button.btn.btn-primary")
    LOCATOR_BUTTON_ALERT_CLOSE = Selector(By.CSS_SELECTOR, "button.close")

    LOCATOR_LINK_FORGOTTEN_PASSWORD = Selector(
        By.LINK_TEXT, "Forgotten Password")

    LOCATOR_ALERT_DANGER_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    LOCATOR_ALERT_SUCCESS_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
'''


class AdminLoginPage(BasePage):

    @property
    def username_input(self):
        return self.page.wait_for_selector("#input-username")

    @property
    def password_input(self):
        return self.page.wait_for_selector("#input-password")

    @property
    def email_input(self):
        return self.page.wait_for_selector("#input-email")

    @property
    def login_button(self):
        return self.page.wait_for_selector("btn btn-primary")

    @property
    def forgotten_password_cancel_button(self):
        return self.page.wait_for_selector("")

    @property
    def forgotten_password_submit_button(self):
        return self.page.wait_for_selector("")

    @property
    def forgotten_password_link(self):
        return self.page.wait_for_selector("")
        self.page.locator()
