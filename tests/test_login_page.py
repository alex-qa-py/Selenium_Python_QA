from page_objects.LoginPage import LoginPage

URL = "/index.php?route=account/login"
PLACEHOLDER_VALUE = "Password"
LOGIN_BUTTON_TITLE = "Login"
RESTORE_PASSWORD_LINK = "https://localhost/opencart/index.php?route=account/forgotten"
RIGHT_COLUMN_LIST_TITLES = ["Login", "Register", "Forgotten Password", "My Account", "Address Book",
                            "Wish List", "Order History", "Downloads", "Recurring payments",
                            "Reward Points", "Returns", "Transactions", "Newsletter"]
ATTRIBUTES = ["placeholder", "value", "href"]
COUNT_OF_MENU_ITEMS = 14


def test_email_input(browser):
    browser.open(URL)
    input_email = LoginPage(browser).email_input()
    assert input_email.is_displayed


def test_password_input(browser):
    browser.open(URL)
    password_input = LoginPage(browser).password_input()

    assert password_input.get_attribute(ATTRIBUTES[0]) == PLACEHOLDER_VALUE


def test_login_button(browser):
    browser.open(URL)
    login_button = LoginPage(browser).login_button()

    assert login_button.get_attribute(ATTRIBUTES[1]) == LOGIN_BUTTON_TITLE


def test_forgotten_password_link(browser):
    browser.open(URL)
    forgotten_password_link = LoginPage(browser).forgotten_password_link()
    assert forgotten_password_link.get_attribute(ATTRIBUTES[2]) == RESTORE_PASSWORD_LINK


def test_list_of_right_column(browser):
    browser.open(URL)
    list_of_right_column = LoginPage(browser).list_of_right_column()
    list_of_titles = []

    for i in list_of_right_column:
        list_of_titles.append(i.text)

    assert list_of_titles == RIGHT_COLUMN_LIST_TITLES
