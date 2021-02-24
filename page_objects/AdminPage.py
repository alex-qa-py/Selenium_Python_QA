from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    RESTORE_PASS_TITLE = (By.CSS_SELECTOR, "span.help-block > a")
    PANEL_TITLE = (By.CSS_SELECTOR, ".panel-title")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    USER_PROFILE = (By.CSS_SELECTOR, "#user-profile")
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "i.fa.fa-sign-out")
    ITEM_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    ITEM_PRODUCTS = (By.XPATH, "//a[text() = \"Products\"]")
    PRODUCTS_TABLE = (By.CSS_SELECTOR, "#form-product")

    def username_input(self):
        return self._wait_for_visible(*self.INPUT_USERNAME)

    def password_input(self):
        return self._wait_for_visible(*self.INPUT_PASSWORD)

    def forgotten_password_link(self):
        return self._wait_for_visible(*self.RESTORE_PASS_TITLE)

    def panel_title(self):
        return self._wait_for_visible(*self.PANEL_TITLE)

    def add_username(self, text):
        self._send_keys(*self.INPUT_USERNAME, text)
        return self

    def add_password(self, text):
        self._send_keys(*self.INPUT_PASSWORD, text)
        return self

    def click_login_button(self):
        self._click(*self.LOGIN_BUTTON)
        return self

    def user_profile(self):
        return self._wait_for_visible(*self.USER_PROFILE)

    def click_log_out(self):
        self._click(*self.LOG_OUT_BUTTON)
        return self

    def click_item_catalog(self):
        self._click(*self.ITEM_CATALOG)
        return self

    def click_item_products(self):
        self._click(*self.ITEM_PRODUCTS)
        return self

    def table(self):
        return self._wait_for_visible(*self.PRODUCTS_TABLE)
