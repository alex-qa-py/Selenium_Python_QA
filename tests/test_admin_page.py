import allure
import helper
from page_objects.AdminPage import AdminPage

ADMIN_PAGE_TITLE = "Administration"
RESTORE_PASS_LINK = f"{helper.get_test_env()}/opencart/admin/index.php?route=common/forgotten"
PANEL_TITLE_DESCRIPTION = "Please enter your login details."
USER_LOGGED_IN = "John Doe"
USER_NAME_ATTR = "alt"

@allure.epic("Admin page")
@allure.description("Checking page title")
def test_title_admin_page(browser):
    AdminPage(browser).open()
    assert browser.title == ADMIN_PAGE_TITLE

@allure.epic("Admin page")
@allure.description("Checking visibility of username input")
def test_username_input(browser):
    page = AdminPage(browser)
    page.open()
    username_input = page.username_input()
    assert username_input.is_displayed()

@allure.epic("Admin page")
@allure.description("Checking visibility of password input")
def test_password_input(browser):
    page = AdminPage(browser)
    page.open()
    username_input = page.password_input()
    assert username_input.is_displayed

@allure.epic("Admin page")
@allure.description("Checking visibility of forgotten password link")
def test_forgotten_password_link(browser):
    page = AdminPage(browser)
    page.open()
    forgotten_password_link = page.forgotten_password_link()

    assert forgotten_password_link.get_attribute(
        "href") == RESTORE_PASS_LINK

@allure.epic("Admin page")
@allure.description("Checking visibility of panel title")
def test_panel_title(browser):
    AdminPage(browser).open()
    panel_title = AdminPage(browser).panel_title()
    assert panel_title.text == PANEL_TITLE_DESCRIPTION

@allure.epic("Admin page")
@allure.description("Checking visibility of admin page title")
def test(browser):
    page = AdminPage(browser)
    page.open()
    page. \
        add_username(helper.get_admin_login()) \
        .add_password(helper.get_admin_pass()) \
        .click_login_button()

    assert page.user_profile().get_attribute(USER_NAME_ATTR) == USER_LOGGED_IN

    page. \
        click_log_out()

    assert browser.title == ADMIN_PAGE_TITLE

@allure.epic("Admin page")
@allure.description("Checking visibility of table \"Products\" with items")
def test_catalog_products(browser):
    page = AdminPage(browser)
    page.open()

    page. \
        add_username(helper.get_admin_login()) \
        .add_password(helper.get_admin_pass()) \
        .click_login_button()

    assert page.user_profile().get_attribute(USER_NAME_ATTR) == USER_LOGGED_IN

    page \
        .click_item_catalog() \
        .click_item_products()

    assert AdminPage(browser).table().is_displayed
