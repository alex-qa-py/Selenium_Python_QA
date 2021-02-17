from selenium.webdriver.common.by import By

from .BasePage import BasePage

class CatalogPage(BasePage):
    PRODUCTS = (By.CSS_SELECTOR, "#content > div > div.product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12")
    LEFT_COLUMN_ITEMS = (By.CSS_SELECTOR,"#column-left > div > a.list-group-item")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR,"#grid-view")
    NAV_BAR_CHAIN = (By.CSS_SELECTOR,"#product-category > ul > li:nth-child(2) > a")
    SORT_BY_INPUT = (By.CSS_SELECTOR,"#input-sort")

    def list_of_products(self):
        return self._elements(*self.PRODUCTS)

    def list_group_item(self):
        return self._elements(*self.LEFT_COLUMN_ITEMS)

    def grid_view(self):
        return self._wait_for_visible(*self.GRID_VIEW_BUTTON)

    def nav_chain(self):
        return self._wait_for_visible(*self.NAV_BAR_CHAIN)

    def select_sort_by(self):
        return self._wait_for_visible(*self.SORT_BY_INPUT)