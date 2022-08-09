from pages.elements.account_dropdown import AccountDropdown
from pages.elements.currency_dropdown import CurrencyDropdown
from pages.store.login_page import CustomerLogin
from pages.store.main_page import MainPage
from frame.classes import Currency
from playwright.sync_api import Page, expect
import pytest
import allure


@allure.feature("Customer side scenarios")
class TestCustomerScenarios:

    @allure.story("Customer UI expirience")
    @allure.title("Customer can change currency")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('cur', (c.name for c in Currency))
    def test_select_currency(self, main_page: MainPage, cur):
        main_page.currency.select(cur)
        expect(main_page.currency.selected).to_have_text(Currency[cur].value)

    @allure.story("Customer's account")
    @allure.title("Customer can login and logout")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_customer_login_and_logout(self, customer_login_page: CustomerLogin, account_valid, db_customer_valid):
        customer_login_page.login_with(account_valid.email, account_valid.password_1)

    @allure.story("Customer's account")
    @allure.title("Customer can restore access to account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_customer_restore_password(self, customer_login_page: CustomerLogin, account_valid, db_customer_valid):
        pass


    @allure.story("Customer's account")
    @allure.title("Customer can register new account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_customer_register(self):
        pass

