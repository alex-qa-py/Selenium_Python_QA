import allure
from selenium.webdriver.common.by import By

import helper
from .BasePage import BasePage


class ProductPage(BasePage):
    URL = f"{helper.get_test_env()}/opencart/index.php?route=product/product&path=57&product_id=49"
    IMAGE = (By.CSS_SELECTOR, ".thumbnail")
    CARD_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    TITLES_TEG = (By.CSS_SELECTOR, "h1")

    @allure.step("Opening url")
    def open(self):
        return self._open(self.URL)

    @allure.step("Waiting for additional images visibility")
    def images_additional(self):
        return self._elements(*self.IMAGE)

    @allure.step("Waiting for product title visibility")
    def product_title(self):
        return self._elements(*self.IMAGE)

    @allure.step("Waiting for quantity  visibility")
    def input_quantity(self):
        return self._wait_for_element_visible(*self.INPUT_QUANTITY)

    @allure.step("Waiting for card button visibility")
    def button_card(self):
        return self._wait_for_element_visible(*self.CARD_BUTTON)

    @allure.step("Waiting for list of titles visibility")
    def titles(self):
        return self._elements(*self.TITLES_TEG)
