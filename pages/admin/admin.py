from pages.base_page import BasePage
from playwright.sync_api import Page


class Admin(BasePage):

    def __init__(self, page: Page, url: str = '/admin'):
        super().__init__(page, url)
        self.Tabs.page = self.page
        self.Navigation.Dashboard.page = self.page
        self.Navigation.Catalog.page = self.page

    @property
    def navigation(self):
        return Admin.Navigation()

    @property
    def tabs(self):
        return Admin.Tabs()

    class Navigation:

        @property
        def catalog(self):
            return Admin.Navigation.Catalog()

        @property
        def dashboard(self):
            return Admin.Navigation.Dashboard()

        class Dashboard:

            page: Page

            @property
            def itself(self):
                return self.page.locator("#menu-dashboard > a")

        class Catalog:

            page: Page

            @property
            def itself(self):
                return self.page.locator("#menu-catalog > a")

            @property
            def categories(self):
                return self.page.locator("a", has_text="Categories")

            @property
            def products(self):
                return self.page.locator("a", has_text="Products")

    class Tabs:

        page: Page

        @property
        def general(self):
            return self.page.locator("a", has_text="General")

        @property
        def data(self):
            return self.page.locator("a", has_text="Data")

        @property
        def links(self):
            return self.page.locator("a", has_text="Links")

        @property
        def attribute(self):
            return self.page.locator("a", has_text="Attribute")

        @property
        def option(self):
            return self.page.locator("a", has_text="Option")

        @property
        def recurring(self):
            return self.page.locator("a", has_text="Recurring")

        @property
        def discount(self):
            return self.page.locator("a", has_text="Discount")

        @property
        def special(self):
            return self.page.locator("a", has_text="Special")

        @property
        def image(self):
            return self.page.locator("a", has_text="Image")

        @property
        def reward_points(self):
            return self.page.locator("a", has_text="Reward Points")

        @property
        def seo(self):
            return self.page.locator("a", has_text="SEO")

        @property
        def design(self):
            return self.page.locator("a", has_text="Design")

    @property
    def add_button(self):
        return self.page.locator("a[data-original-title='Add New']")

    @property
    def copy_button(self):
        return self.page.locator("button[data-original-title='Copy'")

    @property
    def delete_button(self):
        return self.page.locator("button[data-original-title='Delete']")

    @property
    def save_button(self):
        return self.page.locator("button[data-original-title='Save']")

    @property
    def cancel_button(self):
        return self.page.locator("a[data-original-title='Cancel']")

    @property
    def alert_success_message(self):
        return self.page.locator("div.alert.alert-success.alert-dismissible")

    @property
    def alert_danger_message(self):
        return self.page.locator("div.alert.alert-danger.alert-dismissible")

    @property
    def close_alert_button(self):
        return self.page.locator("button.close")
