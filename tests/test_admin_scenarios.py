import allure
import pytest
from frame.classes import ProductData
from pages.admin.account import AccountErrors, AdminAccount
from pages.admin.admin import Admin
from pages.admin.product import AdminProduct
from playwright.sync_api import expect


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
                AccountErrors.TEXT_CONFIRMATION_EMAIL_SENT)

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
                AccountErrors.TEXT_EMAIL_NOT_FOUND)

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
    @allure.story("Product management")
    @allure.title("add new product")
    def test_add_product(self, page, account_admin_valid, product_random: ProductData, db_delete_product):

        login = AdminAccount(page)
        login.open()

        with allure.step("do login with {account_admin_valid}"):
            login.login_with(*account_admin_valid)

        with allure.step("go to product list and click Add button"):
            admin = Admin(page, url=login.url)
            admin.navigation.catalog.itself.click()
            admin.navigation.catalog.products.click()
            admin.add_button.click()

        with allure.step("switch to 'General' tab and fill in the data"):
            product = AdminProduct(page, url=admin.url)
            admin.tabs.general.click()
            product.product.name.fill(product_random.name)
            product.product.description.fill(product_random.description)
            product.product.meta_tag_title.fill(product_random.name)

        with allure.step("switch to 'Data' tab and fill in the data"):
            admin.tabs.data.click()
            product.product.model.fill(product_random.name)
            product.product.price.fill(str(product_random.price))
            product.product.quantity.fill(str(product_random.quantity))

        with allure.step("switch to 'Links' tab and select the product category"):
            admin.tabs.links.click()
            product.fill_with_dropdown(
                locator=product.product.categories, text=product_random.categories)

        with allure.step("save new product"):
            admin.save_button.click()
            expect(admin.alert_success_message).to_be_visible()
            admin.close_alert_button.click()

        with allure.step("do logout"):
            login.logout()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Product management")
    @allure.title("delete test product")
    def test_delete_product(self, page, account_admin_valid, db_product_random):
        login = AdminAccount(page)
        login.open()

        with allure.step("do login with {account_admin_valid}"):
            login.login_with(*account_admin_valid)

        with allure.step("go to product list"):
            admin = Admin(page, url=login.url)
            admin.on("dialog", lambda dialog: dialog.accept())
            admin.navigation.catalog.itself.click()
            admin.navigation.catalog.products.click()

        with allure.step("select products having models like 'test_'"):
            product = AdminProduct(page, url=admin.url)
            product.filter.model.fill('test_')
            product.filter.button.click()
            rows = product.get_products()
            assert rows

        with allure.step("delete all selected products"):
            count = rows.count()
            if count:
                for i in range(rows.count()):
                    product.select_product(rows.nth(i))
                admin.delete_button.click()
                expect(admin.alert_success_message).to_be_visible()
                admin.close_alert_button.click()
            else:
                pytest.fail()

        with allure.step("do logout"):
            login.logout()
