from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helper

URL = "admin/"
ADMIN_PAGE_TITLE = "Administration"
INPUT_USERNAME = "#input-username"
INPUT_PASSWORD = "#input-password"
RESTORE_PASS_TITLE = "span.help-block > a"
RESTORE_PASS_LINK = "https://localhost/opencart/admin/index.php?route=common/forgotten"
PANEL_TITLE = ".panel-title"
PANEL_TITLE_DESCRIPTION = "Please enter your login details."
LOGIN_BUTTON = "button.btn.btn-primary"
USER_PROFILE = "#user-profile"
USER_LOGGED_IN = "John Doe"
LOG_OUT_BUTTON = "i.fa.fa-sign-out"
CATALOG_ITEM = "#menu-catalog"
PRODUCTS_ITEM = "//a[text() = \"Products\"]"
PRODUCTS_TABLE = "#form-product"


def test_title_admin_page(browser):
    browser.get(browser.url + URL)
    assert browser.title == ADMIN_PAGE_TITLE


def test_username_input(browser):
    browser.get(browser.url + URL)
    username_input = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, INPUT_USERNAME)))
    assert username_input[0].is_displayed


def test_password_input(browser):
    browser.get(browser.url + URL)
    username_input = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, INPUT_PASSWORD)))
    assert username_input[0].is_displayed


def test_forgotten_password_link(browser):
    browser.get(browser.url + URL)
    forgotten_password_link = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, RESTORE_PASS_TITLE)))

    assert forgotten_password_link.get_attribute(
        "href") == RESTORE_PASS_LINK


def test_panel_title(browser):
    browser.get(browser.url + URL)
    panel_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, PANEL_TITLE)))
    assert panel_title.text == PANEL_TITLE_DESCRIPTION


"""Task 3 additional tests"""


def test_login(browser):
    browser.get(browser.url + URL)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, INPUT_USERNAME))).send_keys(helper.get_admin_login())

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, INPUT_PASSWORD))).send_keys(helper.get_admin_pass())

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, LOGIN_BUTTON))).click()

    user_profile = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, USER_PROFILE)))

    assert user_profile.get_attribute("alt") == USER_LOGGED_IN

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, LOG_OUT_BUTTON))).click()

    assert browser.title == ADMIN_PAGE_TITLE

def test_catalog_products(browser):
    browser.get(browser.url + URL)
    wait = WebDriverWait(browser, 20)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, INPUT_USERNAME))).send_keys(helper.get_admin_login())

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, INPUT_PASSWORD))).send_keys(helper.get_admin_pass())

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, LOGIN_BUTTON))).click()

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, CATALOG_ITEM))).click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, PRODUCTS_ITEM))).click()

    table = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, PRODUCTS_TABLE)))

    assert table.is_displayed
