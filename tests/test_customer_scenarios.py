from pages.store.account import CustomerAccount
from pages.store.main_page import MainPage
from frame.classes import Currency
from playwright.sync_api import expect
import pytest
import allure


@allure.feature("Customer side scenarios")
class TestCustomerScenarios:

    @allure.story("Customer UI expirience")
    @allure.title("Customer can change currency")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('cur', (c.name for c in Currency))
    def test_select_currency(self, main_page: MainPage, cur):

        with allure.step("select currency {cur}"):
            main_page.currency_dropdown.select(cur)
            expect(main_page.currency_dropdown.selected).to_have_text(
                Currency[cur].value)

    @allure.story("Customer's account")
    @allure.title("Customer can login and logout")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_customer_login_and_logout(self, customer_page: CustomerAccount, account_valid, db_customer_valid):

        with allure.step("login with {account_valid.email} / {account_valid.password_1}"):
            customer_page.login_with(
                account_valid.email, account_valid.password_1)
            expect(customer_page.page).to_have_title(
                customer_page.account_title)

        with allure.step("do logout"):
            customer_page.logout()
            expect(customer_page.page).to_have_title(
                customer_page.logout_title)

    @allure.story("Customer's account")
    @allure.title("Customer can restore access to account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_customer_restore_password(self, customer_page: CustomerAccount, account_valid, db_customer_valid):
        
        with allure.step("navigate to password restore page"):
            customer_page.forgotten_password_link.click()
            expect(customer_page.page).to_have_title(
                customer_page.forgotten_password_title)
        
        with allure.step("try to restore password for {account_valid.email}"):
            customer_page.restore_password(account_valid.email)
            expect(customer_page.alert_success_message).to_be_visible()

    @allure.story("Customer's account")
    @allure.title("Customer can cancel to restore password")
    @allure.severity(allure.severity_level.NORMAL)
    def test_customer_cancel_restore_password(self, customer_page: CustomerAccount):
        
        with allure.step("navigate to password restore page"):
            customer_page.forgotten_password_link.click()
            expect(customer_page.page).to_have_title(
                customer_page.forgotten_password_title)
        
        with allure.step("return back to login page"):
            customer_page.forgotten_password_back_button.click()
            expect(customer_page.page).to_have_title(customer_page.login_title)

    @allure.story("Customer's account")
    @allure.title("Customer can register new account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_customer_register_account(self, customer_page: CustomerAccount):
        pass
