import allure
from playwright.sync_api import expect
from pages.admin.account import AdminAccount


@allure.feature("Admin side scenarios")
class TestAdminLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Admin login scenarios")
    @allure.title("Successful admin login")
    def test_admin_login_successful(self, admin_page: AdminAccount, account_admin_valid):

        with allure.step("Submit login form data"):
            admin_page.login_with(*account_admin_valid)
            expect(admin_page.page).to_have_title(
                admin_page.admin_title)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Admin login scenarios")
    @allure.title("Error of admin login")
    def test_admin_login_error(self, admin_page: AdminAccount, account_admin_invalid):

        with allure.step("Submit login form data"):
            admin_page.login_with(*account_admin_invalid)
            expect(admin_page.page).to_have_title(
                admin_page.login_title)

        with allure.step("Close success alert"):
            expect(admin_page.alert_danger_message).to_contain_text(
                'No match')
            admin_page.close_alert_button.click()
            expect(admin_page.alert_danger_message).not_to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Admin login scenarios")
    @allure.title("Restore admin password with valid email")
    def test_admin_restore_password_with_valid_email(self, admin_page: AdminAccount):

        with allure.step("Submit valid email to form"):
            admin_page.restore_password('user@example.com')
            expect(admin_page.page).to_have_title(
                admin_page.login_title)
            expect(admin_page.alert_success_message).to_contain_text(
                'An email with a confirmation link has been sent')

        with allure.step("Close success alert"):
            admin_page.close_alert_button.click()
            expect(admin_page.alert_success_message).not_to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Admin login scenarios")
    @allure.title("Restore admin password with invalid email")
    def test_admin_restore_password_with_invalid_email(self, admin_page: AdminAccount):

        with allure.step("Submit valid email to form"):
            admin_page.restore_password('user@example.net')
            expect(admin_page.page).to_have_title(
                admin_page.forgotten_password_title)
            expect(admin_page.alert_danger_message).to_contain_text(
                'The E-Mail Address was not found')

        with allure.step("Close danger alert"):
            admin_page.close_alert_button.click()
            expect(admin_page.alert_danger_message).not_to_be_visible()

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("Admin login scenarios")
    @allure.title("Cancel to restore admin password")
    def test_admin_restore_password_cancel(self, admin_page: AdminAccount):

        with allure.step("Go to password restore page"):
            admin_page.forgotten_password_link.click()
            expect(admin_page.page).to_have_title(
                admin_page.forgotten_password_title)

        with allure.step("Cancel to restore password"):
            admin_page.forgotten_password_cancel_button.click()
            expect(admin_page.page).to_have_title(
                admin_page.login_title)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Admin management scenarios")
    @allure.title("")
    def test_admin_add_product(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Admin management scenarios")
    @allure.title("")
    def test_admin_delete_product(self):
        pass
