from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    CONTENT_ROWS = (By.CSS_SELECTOR, ".row")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    LIST_OF_LINKS = (By.CSS_SELECTOR, ".col-sm-3")

    def page(self):
        return self._elements(*self.CONTENT_ROWS)

    def search_button(self):
        return self._wait_for_visible(*self.SEARCH_BUTTON)

    def search_input(self):
        return self._wait_for_visible(*self.SEARCH_INPUT)

    def cart_button(self):
        return self._wait_for_visible(*self.CART_BUTTON)

    def list_of_links(self):
        return self._elements(*self.LIST_OF_LINKS)
