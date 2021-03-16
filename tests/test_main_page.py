import allure

from page_objects.MainPage import MainPage

LINKS_COUNT = 5
ROW_COUNT = 4

@allure.epic("Main page")
@allure.description("Checking rowcount of content rows")
def test_page(browser):
    page = MainPage(browser)
    page.open()
    class_row = page.page()
    assert len(class_row) == ROW_COUNT

@allure.epic("Main page")
@allure.description("Checking is_enabled of search button")
def test_search_button(browser):
    page = MainPage(browser)
    page.open()
    button = page.search_button()
    assert button.is_enabled()

@allure.epic("Main page")
@allure.description("Checking visibility of search input")
def test_search_input(browser):
    page = MainPage(browser)
    page.open()
    search_input = page.search_input()
    assert search_input.is_displayed()


@allure.epic("Main page")
@allure.description("Checking is_enabled of cart button")
def test_cart_button(browser):
    page = MainPage(browser)
    page.open()
    cart = page.cart_button()
    assert cart.is_enabled()

@allure.epic("Main page")
@allure.description("Checking count of search button")
def test_list_of_links(browser):
    page = MainPage(browser)
    page.open()
    list_of_links = page.list_of_links()
    assert len(list_of_links) == LINKS_COUNT
