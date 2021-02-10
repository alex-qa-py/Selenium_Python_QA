from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CONTENT_ROWS = ".row"
ROW_COUNT = 4
SEARCH_BUTTON = ".input-group-btn"
SEARCH_INPUT = "#search"
CART_BUTTON = "#cart"
LIST_OF_LINKS = ".col-sm-3"
LINKS_COUNT = 5

def test_page(browser):
    class_row = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, CONTENT_ROWS)))
    assert len(class_row) == ROW_COUNT


def test_search_button(browser):
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, SEARCH_BUTTON)))
    assert button.is_enabled()


def test_search_input(browser):
    search_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, SEARCH_INPUT)))
    assert search_input.is_displayed()


def test_cart(browser):
    cart = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, CART_BUTTON)))
    assert cart.is_enabled()


def test_list_of_links(browser):
    list_of_links = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, LIST_OF_LINKS)))
    assert len(list_of_links) == LINKS_COUNT
