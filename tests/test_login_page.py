import allure

import helper
from page_objects.LoginPage import LoginPage

PLACEHOLDER_VALUE = "Password"
LOGIN_BUTTON_TITLE = "Login"
RESTORE_PASSWORD_LINK = f"{helper.get_test_env()}/opencart/index.php?route=account/forgotten"
RIGHT_COLUMN_LIST_TITLES = ["Login", "Register", "Forgotten Password", "My Account", "Address Book",
                            "Wish List", "Order History", "Downloads", "Recurring payments",
                            "Reward Points", "Returns", "Transactions", "Newsletter"]
ATTRIBUTES = ["placeholder", "value", "href"]
COUNT_OF_MENU_ITEMS = 14

@allure.epic("Login page")
@allure.description("Checking visibility of email input")
def test_email_input(browser):
    page = LoginPage(browser)
    page.open()
    input_email = page.email_input()
    assert input_email.is_displayed


@allure.epic("Login page")
@allure.description("Checking attribute placeholder of password input")
def test_password_input(browser):
    page = LoginPage(browser)
    page.open()
    password_input = page.password_input()

    assert password_input.get_attribute(ATTRIBUTES[0]) == PLACEHOLDER_VALUE


@allure.epic("Login page")
@allure.description("Checking attribute value of login input")
def test_login_button(browser):
    page = LoginPage(browser)
    page.open()
    login_button = page.login_button()

    assert login_button.get_attribute(ATTRIBUTES[1]) == LOGIN_BUTTON_TITLE

@allure.epic("Login page")
@allure.description("Checking attribute href of email input")
def test_forgotten_password_link(browser):
    page = LoginPage(browser)
    page.open()
    forgotten_password_link = page.forgotten_password_link()
    assert forgotten_password_link.get_attribute(ATTRIBUTES[2]) == RESTORE_PASSWORD_LINK

@allure.epic("Login page")
@allure.description("Matching list of titles and titles in right column")
def test_list_of_right_column(browser):
    page = LoginPage(browser)
    page.open()
    list_of_right_column = page.list_of_right_column()
    list_of_titles = []

    for i in list_of_right_column:
        list_of_titles.append(i.text)

    assert list_of_titles == RIGHT_COLUMN_LIST_TITLES
