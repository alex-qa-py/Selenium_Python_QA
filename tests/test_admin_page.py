import helper
from page_objects.AdminPage import AdminPage

URL = "admin/"
ADMIN_PAGE_TITLE = "Administration"
RESTORE_PASS_LINK = "https://localhost/opencart/admin/index.php?route=common/forgotten"
PANEL_TITLE_DESCRIPTION = "Please enter your login details."
USER_LOGGED_IN = "John Doe"
USER_NAME_ATTR = "alt"


def test_title_admin_page(browser):
    browser.open(URL)
    assert browser.title == ADMIN_PAGE_TITLE


def test_username_input(browser):
    browser.open(URL)
    username_input = AdminPage(browser).username_input()
    assert username_input.is_displayed


def test_password_input(browser):
    browser.open(URL)
    username_input = AdminPage(browser).password_input()
    assert username_input.is_displayed


def test_forgotten_password_link(browser):
    browser.open(URL)
    forgotten_password_link = AdminPage(browser).forgotten_password_link()

    assert forgotten_password_link.get_attribute(
        "href") == RESTORE_PASS_LINK


def test_panel_title(browser):
    browser.open(URL)
    panel_title = AdminPage(browser).panel_title()
    assert panel_title.text == PANEL_TITLE_DESCRIPTION


def test(browser):
    browser.open(URL)
    action = AdminPage(browser)
    action. \
        add_username(helper.get_admin_login()) \
        .add_password(helper.get_admin_pass()) \
        .click_login_button()

    assert action.user_profile().get_attribute(USER_NAME_ATTR) == USER_LOGGED_IN

    action. \
        click_log_out()

    assert browser.title == ADMIN_PAGE_TITLE


def test_catalog_products(browser):
    browser.open(URL)
    action = AdminPage(browser)
    action. \
        add_username(helper.get_admin_login()) \
        .add_password(helper.get_admin_pass()) \
        .click_login_button()

    assert action.user_profile().get_attribute(USER_NAME_ATTR) == USER_LOGGED_IN

    action \
        .click_item_catalog() \
        .click_item_products()

    assert action.table().is_displayed
