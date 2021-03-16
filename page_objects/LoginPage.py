import allure
from selenium.webdriver.common.by import By

import helper
from .BasePage import BasePage


class LoginPage(BasePage):
    URL = f"{helper.get_test_env()}/opencart/index.php?route=account/login"
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    RESTORE_PASSWORD = (By.CSS_SELECTOR, "div.form-group > a")
    RIGHT_COLUMN_LIST = (By.CSS_SELECTOR, "#column-right > div > a")

    @allure.step("Opening url")
    def open(self):
        return self._open(self.URL)

    @allure.step("Waiting for email input visibility")
    def email_input(self):
        return self._wait_for_element_visible(*self.INPUT_EMAIL)

    @allure.step("Waiting for password input visibility")
    def password_input(self):
        return self._wait_for_element_visible(*self.INPUT_PASSWORD)

    @allure.step("Waiting for login button visibility")
    def login_button(self):
        return self._wait_for_element_visible(*self.LOGIN_BUTTON)

    @allure.step("Waiting for forgotten link visibility")
    def forgotten_password_link(self):
        return self._wait_for_element_visible(*self.RESTORE_PASSWORD)

    @allure.step("Waiting for right column list visibility")
    def list_of_right_column(self):
        return self._elements(*self.RIGHT_COLUMN_LIST)
