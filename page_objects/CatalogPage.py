import allure
from selenium.webdriver.common.by import By

import helper
from .BasePage import BasePage


class CatalogPage(BasePage):
    URL = f"{helper.get_test_env()}/opencart/index.php?route=product/category&path=20"
    PRODUCTS = (
        By.CSS_SELECTOR, "#content > div > div.product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12")
    LEFT_COLUMN_ITEMS = (By.CSS_SELECTOR, "#column-left > div > a.list-group-item")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    NAV_BAR_CHAIN = (By.CSS_SELECTOR, "#product-category > ul > li:nth-child(2) > a")
    SORT_BY_INPUT = (By.CSS_SELECTOR, "#input-sort")

    @allure.step("Opening url")
    def open(self):
        return self._open(self.URL)

    @allure.step("Waiting for list of products elements")
    def list_of_products(self):
        return self._elements(*self.PRODUCTS)

    @allure.step("Waiting for group items elements")
    def list_group_item(self):
        return self._elements(*self.LEFT_COLUMN_ITEMS)

    @allure.step("Waiting for grid button visibility")
    def grid_view(self):
        return self._wait_for_element_visible(*self.GRID_VIEW_BUTTON)

    @allure.step("Waiting for navigation chain visibility")
    def nav_chain(self):
        return self._wait_for_element_visible(*self.NAV_BAR_CHAIN)

    @allure.step("Waiting for sort input visibility")
    def select_sort_by(self):
        return self._wait_for_element_visible(*self.SORT_BY_INPUT)
