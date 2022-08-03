import allure
from playwright.sync_api import expect
from pages.admin.login_page import AdminLogin


@allure.feature("Admin side scenarios")
@allure.story("Admin login scenarios")
class TestAdminScenarios:

    @allure.title("Successful admin login")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_admin_login_successful(self, admin_login_page: AdminLogin, account_admin_valid):

        with allure.step("Submit login form data"):
            admin_login_page.login_with(*account_admin_valid)
            expect(admin_login_page.page).to_have_title(
                admin_login_page.admin_title)

    @allure.title("Error of admin login")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_admin_login_error(self, admin_login_page: AdminLogin, account_admin_invalid):

        with allure.step("Submit login form data"):
            admin_login_page.login_with(*account_admin_invalid)
            expect(admin_login_page.page).to_have_title(
                admin_login_page.login_title)

        with allure.step("Close success alert"):
            expect(admin_login_page.alert_danger_message).to_contain_text(
                'No match')
            admin_login_page.close_alert_button.click()
            expect(admin_login_page.alert_danger_message).not_to_be_visible()

    @allure.title("Restore admin password with valid email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_admin_restore_password_with_valid_email(self, admin_login_page: AdminLogin):

        with allure.step("Submit valid email to form"):
            admin_login_page.restore_password('user@example.com')
            expect(admin_login_page.page).to_have_title(
                admin_login_page.login_title)
            expect(admin_login_page.alert_success_message).to_contain_text(
                'An email with a confirmation link has been sent')

        with allure.step("Close success alert"):
            admin_login_page.close_alert_button.click()
            expect(admin_login_page.alert_success_message).not_to_be_visible()

    @allure.title("Restore admin password with invalid email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_admin_restore_password_with_invalid_email(self, admin_login_page: AdminLogin):

        with allure.step("Submit valid email to form"):
            admin_login_page.restore_password('user@example.net')
            expect(admin_login_page.page).to_have_title(
                admin_login_page.forgotten_password_title)
            expect(admin_login_page.alert_danger_message).to_contain_text(
                'The E-Mail Address was not found')

        with allure.step("Close danger alert"):
            admin_login_page.close_alert_button.click()
            expect(admin_login_page.alert_danger_message).not_to_be_visible()

    @allure.title("Cancel to restore admin password")
    @allure.severity(allure.severity_level.MINOR)
    def test_admin_restore_password_cancel(self, admin_login_page: AdminLogin):

        with allure.step("Go to password restore page"):
            admin_login_page.forgotten_password_link.click()
            expect(admin_login_page.page).to_have_title(
                admin_login_page.forgotten_password_title)

        with allure.step("Cancel to restore password"):
            admin_login_page.forgotten_password_cancel_button.click()
            expect(admin_login_page.page).to_have_title(
                admin_login_page.login_title)
