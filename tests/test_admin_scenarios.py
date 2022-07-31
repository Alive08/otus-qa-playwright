from playwright.sync_api import expect
from pages.admin.login_page import AdminLogin


def test_admin_login_successful(admin_login_page: AdminLogin, account_admin_valid):
    admin_login_page.login_with(*account_admin_valid)
    expect(admin_login_page.page).to_have_title(admin_login_page.admin_title)


def test_admin_login_error(admin_login_page: AdminLogin, account_admin_invalid):
    admin_login_page.login_with(*account_admin_invalid)
    expect(admin_login_page.page).to_have_title(admin_login_page.login_title)
    expect(admin_login_page.alert_danger_message).to_contain_text('No match')
    admin_login_page.close_alert_button.click()
    expect(admin_login_page.alert_danger_message).not_to_be_visible()


def test_admin_restore_password_with_valid_email(admin_login_page: AdminLogin):
    admin_login_page.restore_password('user@example.com')
    expect(admin_login_page.page).to_have_title(admin_login_page.login_title)
    expect(admin_login_page.alert_success_message).to_contain_text(
        'An email with a confirmation link has been sent')
    admin_login_page.close_alert_button.click()
    expect(admin_login_page.alert_success_message).not_to_be_visible()


def test_admin_restore_password_with_invalid_email(admin_login_page: AdminLogin):
    admin_login_page.restore_password('user@example.net')
    expect(admin_login_page.page).to_have_title(admin_login_page.forgotten_password_title)
    expect(admin_login_page.alert_danger_message).to_contain_text(
        'The E-Mail Address was not found')
    admin_login_page.close_alert_button.click()
    expect(admin_login_page.alert_danger_message).not_to_be_visible()


def test_admin_restore_password_cancel(admin_login_page: AdminLogin):
    admin_login_page.forgotten_password_link.click()
    expect(admin_login_page.page).to_have_title(admin_login_page.forgotten_password_title)
    admin_login_page.forgotten_password_cancel_button.click()
    expect(admin_login_page.page).to_have_title(admin_login_page.login_title)
