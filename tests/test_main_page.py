from page_objects.MainPage import MainPage

LINKS_COUNT = 5
ROW_COUNT = 4


def test_page(browser):
    browser.open("")
    class_row = MainPage(browser).page()
    assert len(class_row) == ROW_COUNT


def test_search_button(browser):
    browser.open("")
    button = MainPage(browser).search_button()
    assert button.is_enabled()


def test_search_input(browser):
    browser.open("")
    search_input = MainPage(browser).search_input()
    assert search_input.is_displayed()


def test_cart_button(browser):
    browser.open("")
    cart = MainPage(browser).cart_button()
    assert cart.is_enabled()


def test_list_of_links(browser):
    browser.open("")
    list_of_links = MainPage(browser).list_of_links()
    assert len(list_of_links) == LINKS_COUNT
