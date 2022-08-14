import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
'''


class AdminPageLocators(BaseLocator):

    LOCATOR_ADD = Selector(By.CSS_SELECTOR, "a[data-original-title='Add New']")
    LOCATOR_COPY = Selector(
        By.CSS_SELECTOR, "button[data-original-title='Copy'")
    LOCATOR_DELETE = Selector(
        By.CSS_SELECTOR, "button[data-original-title='Delete']")
    LOCATOR_SAVE = Selector(
        By.CSS_SELECTOR, "button[data-original-title='Save']")
    LOCATOR_CANCEL = Selector(
        By.CSS_SELECTOR, "a[data-original-title='Cancel']")
    LOCATOR_ALERT_DANGER_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    LOCATOR_ALERT_SUCCESS_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    LOCATOR_BUTTON_ALERT_CLOSE = Selector(By.CSS_SELECTOR, "button.close")

    class tabs(Node):
        general = (By.LINK_TEXT, 'General')
        data = (By.LINK_TEXT, 'Data')
        links = (By.LINK_TEXT, 'Links')
        attribute = (By.LINK_TEXT, 'Attribute')
        option = (By.LINK_TEXT, 'Option')
        recurring = (By.LINK_TEXT, 'Recurring')
        discount = (By.LINK_TEXT, 'Discount')
        special = (By.LINK_TEXT, 'Special')
        image = (By.LINK_TEXT, 'Image')
        reward_points = (By.LINK_TEXT, 'Reward Points')
        seo = (By.LINK_TEXT, 'SEO')
        design = (By.LINK_TEXT, 'Design')
'''


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
