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
    def login_title(self):
        return "Administration"

    @property
    def admin_title(self):
        return "Dashboard"

    @property
    def forgotten_password_title(self):
        return "Forgot Your Password?"

    @property
    def username_input(self):
        return self.page.locator("#input-username")

    @property
    def password_input(self):
        return self.page.locator("#input-password")

    @property
    def email_input(self):
        return self.page.locator("#input-email")

    @property
    def login_button(self):
        return self.page.locator('button:has-text("Login")')

    @property
    def forgotten_password_cancel_button(self):
        return self.page.locator("a.btn.btn-default")

    @property
    def forgotten_password_submit_button(self):
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

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def restore_password(self, email):
        self.forgotten_password_link.click()
        self.email_input.fill(email)
        self.forgotten_password_submit_button.click()
