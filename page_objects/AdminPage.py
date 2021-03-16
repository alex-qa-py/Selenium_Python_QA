import allure
from selenium.webdriver.common.by import By

import helper
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    URL = f"{helper.get_test_env()}/opencart/admin/"
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

    @allure.step("Opening url")
    def open(self):
        return self._open(self.URL)

    @allure.step("Waiting for username input visibility")
    def username_input(self):
        return self._wait_for_element_visible(*self.INPUT_USERNAME)

    @allure.step("Waiting for password input visibility")
    def password_input(self):
        return self._wait_for_element_visible(*self.INPUT_PASSWORD)

    @allure.step("Waiting link visibility")
    def forgotten_password_link(self):
        return self._wait_for_element_visible(*self.RESTORE_PASS_TITLE)

    @allure.step("Waiting for title visibility")
    def panel_title(self):
        return self._wait_for_element_visible(*self.PANEL_TITLE)

    @allure.step("Sending keys {text} from username input")
    def add_username(self, text):
        self._send_keys(*self.INPUT_USERNAME, text)
        return self

    @allure.step("Sending keys {text} from password input")
    def add_password(self, text):
        self._send_keys(*self.INPUT_PASSWORD, text)
        return self

    @allure.step("Clicking on the login button")
    def click_login_button(self):
        self._click(*self.LOGIN_BUTTON)
        return self

    @allure.step("Waiting for user profile visibility")
    def user_profile(self):
        return self._wait_for_element_visible(*self.USER_PROFILE)

    @allure.step("Clicking on the logout button")
    def click_log_out(self):
        self._click(*self.LOG_OUT_BUTTON)
        return self

    @allure.step("Clicking on the catalog item ")
    def click_item_catalog(self):
        self._click(*self.ITEM_CATALOG)
        return self

    @allure.step("Clicking on the \"Products\"")
    def click_item_products(self):
        self._click(*self.ITEM_PRODUCTS)
        return self

    @allure.step("Waiting for table with products visibility")
    def table(self):
        return self._wait_for_element_visible(*self.PRODUCTS_TABLE)
