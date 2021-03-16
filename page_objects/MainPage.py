import allure
from selenium.webdriver.common.by import By

import helper
from .BasePage import BasePage


class MainPage(BasePage):
    URL = f"{helper.get_test_env()}/opencart/"
    CONTENT_ROWS = (By.CSS_SELECTOR, ".row")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    LIST_OF_LINKS = (By.CSS_SELECTOR, ".col-sm-3")

    @allure.step("Opening url")
    def open(self):
        return self._open(self.URL)

    @allure.step("Waiting for rows with content elements")
    def page(self):
        return self._elements(*self.CONTENT_ROWS)

    @allure.step("Waiting for search button visibility")
    def search_button(self):
        return self._wait_for_element_visible(*self.SEARCH_BUTTON)

    @allure.step("Waiting for search input visibility")
    def search_input(self):
        return self._wait_for_element_visible(*self.SEARCH_INPUT)

    @allure.step("Waiting for cart button visibility")
    def cart_button(self):
        return self._wait_for_element_visible(*self.CART_BUTTON)

    @allure.step("Waiting for list of links elements")
    def list_of_links(self):
        return self._elements(*self.LIST_OF_LINKS)
