from pages.base_page import BasePage


class AdminLogin(BasePage):

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

    def login_with(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def restore_password(self, email):
        self.forgotten_password_link.click()
        self.email_input.fill(email)
        self.forgotten_password_submit_button.click()
