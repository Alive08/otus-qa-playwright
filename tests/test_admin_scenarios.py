from playwright.sync_api import expect
from pages.admin.login_page import AdminLoginPage


def test_admin_login_successful(login_page: AdminLoginPage, account_admin_valid):
    login_page.login(*account_admin_valid)
    expect(login_page.page).to_have_title(login_page.admin_title)


def test_admin_login_error(login_page: AdminLoginPage, account_admin_invalid):
    login_page.login(*account_admin_invalid)
    expect(login_page.page).to_have_title(login_page.login_title)
    expect(login_page.alert_danger_message).to_contain_text('No match')
    login_page.close_alert_button.click()
    expect(login_page.alert_danger_message).not_to_be_visible()


def test_admin_restore_password_with_valid_email(login_page: AdminLoginPage):
    login_page.restore_password('user@example.com')
    expect(login_page.page).to_have_title(login_page.login_title)
    expect(login_page.alert_success_message).to_contain_text(
        'An email with a confirmation link has been sent')
    login_page.close_alert_button.click()
    expect(login_page.alert_success_message).not_to_be_visible()


def test_admin_restore_password_with_invalid_email(login_page: AdminLoginPage):
    login_page.restore_password('user@example.net')
    expect(login_page.page).to_have_title(login_page.forgotten_password_title)
    expect(login_page.alert_danger_message).to_contain_text(
        'The E-Mail Address was not found')
    login_page.close_alert_button.click()
    expect(login_page.alert_danger_message).not_to_be_visible()


def test_admin_restore_password_cancel(login_page: AdminLoginPage):
    login_page.forgotten_password_link.click()
    expect(login_page.page).to_have_title(login_page.forgotten_password_title)
    login_page.forgotten_password_cancel_button.click()
    expect(login_page.page).to_have_title(login_page.login_title)
