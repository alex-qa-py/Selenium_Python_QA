from selenium.webdriver.common.by import By

from .BasePage import BasePage


class LoginPage(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    RESTORE_PASSWORD = (By.CSS_SELECTOR, "div.form-group > a")
    RIGHT_COLUMN_LIST = (By.CSS_SELECTOR, "#column-right > div > a")

    def email_input(self):
        return self._wait_for_visible(*self.INPUT_EMAIL)

    def password_input(self):
        return self._wait_for_visible(*self.INPUT_PASSWORD)

    def login_button(self):
        return self._wait_for_visible(*self.LOGIN_BUTTON)

    def forgotten_password_link(self):
        return self._wait_for_visible(*self.RESTORE_PASSWORD)

    def list_of_right_column(self):
        return self._elements(*self.RIGHT_COLUMN_LIST)
