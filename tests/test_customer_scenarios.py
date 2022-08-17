import allure
import pytest
from frame.classes import AccountData, Currency
from pages.customer.account import AccountErrors, CustomerAccount
from pages.customer.main_page import MainPage
from playwright.sync_api import expect


@allure.feature("Customer side scenarios")
class TestCustomerScenarios:

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer UI expirience")
    @allure.title("Customer can change currency")
    @pytest.mark.parametrize('cur', (c.name for c in Currency))
    def test_select_currency(self, main_page: MainPage, cur):

        with allure.step(f"select currency {cur}"):
            main_page.currency_dropdown.select(cur)
            expect(main_page.currency_dropdown.selected).to_have_text(
                Currency[cur].value)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Customer's account")
    @allure.title("Customer can login and logout")
    def test_customer_login_and_logout(self, customer_page: CustomerAccount, account_valid: AccountData, db_customer_valid):

        with allure.step(f"login with {account_valid.email} / {account_valid.password_1}"):
            customer_page.login_with(
                account_valid.email, account_valid.password_1)
            expect(customer_page.page).to_have_title(
                customer_page.account_title)

        with allure.step("do logout"):
            customer_page.logout()
            expect(customer_page.page).to_have_title(
                customer_page.logout_title)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer's account")
    @allure.title("Customer can restore access to account")
    def test_customer_restore_password(self, customer_page: CustomerAccount, account_valid: AccountData, db_customer_valid):

        with allure.step("navigate to password restore page"):
            customer_page.forgotten_password_link.click()
            expect(customer_page.page).to_have_title(
                customer_page.forgotten_password_title)

        with allure.step(f"try to restore password for {account_valid.email}"):
            customer_page.restore_password(account_valid.email)
            expect(customer_page.alert_success_message).to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer's account")
    @allure.title("Customer can cancel to restore password")
    def test_customer_cancel_restore_password(self, customer_page: CustomerAccount):

        with allure.step("navigate to password restore page"):
            customer_page.forgotten_password_link.click()
            expect(customer_page.page).to_have_title(
                customer_page.forgotten_password_title)

        with allure.step("return back to login page"):
            customer_page.forgotten_password_back_button.click()
            expect(customer_page.page).to_have_title(customer_page.login_title)

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("Customer's account")
    @allure.title("Read Privacy policy")
    def test_read_privacy_policy(self, customer_page: CustomerAccount):
        customer_page.new_account_continue_button.click()
        customer_page.privacy_policy_link.click()
        customer_page.close_alert_button.click()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer's account")
    @allure.title("Check and uncheck the 'agree' checkbox")
    def test_check_agree(self, customer_page: CustomerAccount):
        customer_page.new_account_continue_button.click()
        customer_page.privacy_policy_box.check()
        expect(customer_page.privacy_policy_box).to_be_checked()
        customer_page.privacy_policy_box.uncheck()
        expect(customer_page.privacy_policy_box).not_to_be_checked()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Customer's account")
    @allure.title("Register account with valid data")
    def test_register_account(self, customer_page: CustomerAccount, account_valid: AccountData, db_delete_customer_valid):
        customer_page.new_account_continue_button.click()

        with allure.step("submit registration form"):
            customer_page.register_account(account_valid)
            expect(customer_page.page.locator("h1")).to_have_text(
                AccountErrors.TEXT_ACCOUNT_CREATED)

        with allure.step("do logout"):
            customer_page.logout()
            expect(customer_page.page).to_have_title(
                customer_page.logout_title)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Customer's account")
    @allure.title("Try to register account for existent customer")
    def test_register_account_duplicate_data(self, customer_page: CustomerAccount, account_valid: AccountData, db_customer_valid):
        customer_page.new_account_continue_button.click()

        with allure.step("submit registration form"):
            customer_page.register_account(account_valid)
            expect(customer_page.alert_danger_message).to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer's account")
    @allure.title("Try to submit registration form with 'privacy policy' unchecked")
    def test_register_account_privacy_policy_unchecked(self, customer_page: CustomerAccount, account_random: AccountData):
        account_random.password_2 = account_random.password_1
        customer_page.new_account_continue_button.click()

        with allure.step("submit registration form"):
            customer_page.register_account(account_random, agree=False)
            expect(customer_page.alert_danger_message).to_be_visible()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer's account")
    @allure.title("Try to register account with mismatched passwords in the form")
    def test_register_passwords_mismatch(self, customer_page: CustomerAccount, account_random: AccountData):
        customer_page.new_account_continue_button.click()
        account_random.password_2 = ''

        with allure.step("submit registration form"):
            customer_page.register_account(account_random)
            expect(customer_page.text_danger).to_have_text(
                AccountErrors.TEXT_PASSWORDS_MISMATCH)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Customer's account")
    @allure.title("Try to register account with errors in the registration form")
    @pytest.mark.parametrize('field, expected', (('fname', AccountErrors.TEXT_FIRST_NAME_ERROR),
                                                 ('lname', AccountErrors.TEXT_LAST_NAME_ERROR),
                                                 ('email', AccountErrors.TEXT_EMAIL_ERROR),
                                                 ('phone', AccountErrors.TEXT_TELEPHONE_ERROR),
                                                 ('password_1', AccountErrors.TEXT_PASSWORD_ERROR)))
    def test_try_register_account_with_errors(self, customer_page: CustomerAccount, account_random: AccountData, field, expected):
        account_random.password_2 = account_random.password_1
        setattr(account_random, field, '')
        customer_page.new_account_continue_button.click()

        with allure.step(f"submit registration form with empty field {field}"):
            customer_page.register_account(account_random)
            expect(customer_page.text_danger.first).to_have_text(expected)
