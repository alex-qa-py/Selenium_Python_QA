from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ProductPage(BasePage):
    IMAGE = (By.CSS_SELECTOR, ".thumbnail")
    CARD_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    TITLES_TEG = (By.CSS_SELECTOR, "h1")

    def images_additional(self):
        return self._elements(*self.IMAGE)

    def product_title(self):
        return self._elements(*self.IMAGE)

    def input_quantity(self):
        return self._wait_for_visible(*self.INPUT_QUANTITY)

    def button_card(self):
        return self._wait_for_visible(*self.CARD_BUTTON)

    def titles(self):
        return self._elements(*self.TITLES_TEG)
