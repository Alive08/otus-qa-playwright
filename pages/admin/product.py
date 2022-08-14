from playwright.sync_api import Locator
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class AdminProduct(BasePage):

    def __init__(self, page: Page, url: str = '/admin'):
        super().__init__(page, url)
        self.Filter.page = self.page
        self.Product.page = self.page
        self.ProductRows.page = self.page

    @property
    def product(self):
        return AdminProduct.Product()

    @property
    def filter(self):
        return AdminProduct.Filter()

    @property
    def product_rows(self):
        return AdminProduct.ProductRows()

    class Product:

        page: Page

        @property
        def name(self):
            return self.page.locator("#form-product > * #input-name1")

        @property
        def description(self):
            return self.page.locator("#form-product > * div.note-editable")

        @property
        def meta_tag_title(self):
            return self.page.locator("#form-product > * #input-meta-title1")

        @property
        def model(self):
            return self.page.locator("#form-product > * #input-model")

        @property
        def price(self):
            return self.page.locator("#form-product > * #input-price")

        @property
        def quantity(self):
            return self.page.locator("#form-product > * #input-quantity")

        @property
        def manufacturer(self):
            return self.page.locator("#form-product > * #input-manufacturer")

        @property
        def categories(self):
            return self.page.locator("#form-product > * #input-category")

    class Filter:

        page: Page

        @property
        def name(self):
            return self.page.locator("#filter-product > * #input-name")

        @property
        def model(self):
            return self.page.locator("#filter-product > * #input-model")

        @property
        def price(self):
            return self.page.locator("#filter-product > * #input-price")

        @property
        def quantity(self):
            return self.page.locator("#filter-product > * input-quantity")

        @property
        def status(self):
            return self.page.locator("#filter-product > * input-status")

        @property
        def button(self):
            return self.page.locator("#filter-product > * #button-filter")

    class ProductRows:

        page: Page

        @property
        def itself(self):
            return self.page.locator("#form-product > * table > tbody > tr")

        @property
        def checkbox(self):
            return "td > input[type='checkbox']"

        @property
        def name(self):
            return "td:nth-child(2)"

        @property
        def no_result(self):
            return self.page.locator("#form-product > * table > tbody  > tr > td[colspan='8']")

    @allure.step("get all products from list")
    def get_products(self) -> Locator:
        self._logger.info("get all products from list")
        if not self.product_rows.no_result.is_visible(timeout=5):
            return self.product_rows.itself

    @allure.step("get product name")
    def get_product_name(self, row: Locator):
        self._logger.info("get product name")
        return row.locator(self.product_rows.name).text_content()

    @allure.step("select product")
    def select_product(self, row: Locator):
        self._logger.info("select product")
        row.locator(self.product_rows.checkbox).check()
