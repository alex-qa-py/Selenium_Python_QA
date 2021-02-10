from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "/index.php?route=product/category&path=20"
PRODUCTS = "#content > div > div.product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12"
LEFT_COLUMN_ITEMS = "#column-left > div > a.list-group-item"
GRID_VIEW_BUTTON = "#grid-view"
NAV_BAR_CHAIN = "#product-category > ul > li:nth-child(2) > a"
NAV_BAR_NAME = "Desktops"
SORT_BY_INPUT = "#input-sort"
PRODUCT_COUNT = 12
COUNT_OF_LEFT_COLUMN_ITEMS = 10


def test_product_count(browser):
    browser.get(browser.url + URL)
    list_of_products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, PRODUCTS)))
    assert len(list_of_products) == PRODUCT_COUNT


def test_list_group_item(browser):
    browser.get(browser.url + URL)
    list_group_item = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, LEFT_COLUMN_ITEMS)))
    assert len(list_group_item) == COUNT_OF_LEFT_COLUMN_ITEMS


def test_grid_view(browser):
    browser.get(browser.url + URL)
    grid_view_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, GRID_VIEW_BUTTON)))
    assert grid_view_button.is_displayed()


def test_nav_chain(browser):
    browser.get(browser.url + URL)
    nav_chain = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, NAV_BAR_CHAIN)))
    assert nav_chain.text == NAV_BAR_NAME


def test_select_sort_by(browser):
    browser.get(browser.url + URL)
    select_sort_by = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, SORT_BY_INPUT)))
    assert select_sort_by.is_enabled()
