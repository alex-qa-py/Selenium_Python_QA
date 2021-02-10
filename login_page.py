from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "/index.php?route=account/login"
INPUT_EMAIL = "#input-email"
INPUT_PASSWORD = "#input-password"
PLACEHOLDER_VALUE = "Password"
LOGIN_BUTTON = "input.btn.btn-primary"
LOGIN_BUTTON_TITLE = "Login"
RESTORE_PASSWORD = "div.form-group > a"
RESTORE_PASSWORD_LINK = "https://localhost/opencart/index.php?route=account/forgotten"
RIGHT_COLUMN_LIST = "#column-right > div > a"
RIGHT_COLUMN_LIST_TITLES = ["Login", "Register", "Forgotten Password", "My Account", "Address Book",
                                         "Wish List", "Order History", "Downloads", "Recurring payments",
                                         "Reward Points", "Returns", "Transactions", "Newsletter"]
ATTRIBUTES = ["placeholder", "value", "href"]


def test_email_input(browser):
    browser.get(browser.url + URL)
    input_email = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, INPUT_EMAIL)))
    assert input_email.is_displayed


def test_password_input(browser):
    browser.get(browser.url + URL)
    password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, INPUT_PASSWORD)))

    assert password_input.get_attribute(ATTRIBUTES[0]) == PLACEHOLDER_VALUE


def test_login_button(browser):
    browser.get(browser.url + URL)
    login_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, LOGIN_BUTTON)))

    assert login_button.get_attribute(ATTRIBUTES[1]) == LOGIN_BUTTON_TITLE


def test_forgotten_password_link(browser):
    browser.get(browser.url + URL)
    forgotten_password_link = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, RESTORE_PASSWORD)))

    assert forgotten_password_link.get_attribute(ATTRIBUTES[2]) == RESTORE_PASSWORD_LINK


def test_list_of_right_column(browser):
    browser.get(browser.url + URL)
    list_of_right_column = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, RIGHT_COLUMN_LIST)))

    list_of_titles = []
    for i in list_of_right_column:
        list_of_titles.append(i.text)

    assert list_of_titles == RIGHT_COLUMN_LIST_TITLES
