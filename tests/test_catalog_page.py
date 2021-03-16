import allure

from page_objects.CatalogPage import CatalogPage

PRODUCT_COUNT = 12
COUNT_OF_LEFT_COLUMN_ITEMS = 10
NAV_BAR_NAME = "Desktops"

@allure.epic("Catalog page")
@allure.description("Checking count of items in list of products")
def test_product_count(browser):
    page = CatalogPage(browser)
    page.open()
    list_of_products = page.list_of_products()
    assert len(list_of_products) == PRODUCT_COUNT

@allure.epic("Catalog page")
@allure.description("Checking count of items in list of groups")
def test_list_group_item(browser):
    page = CatalogPage(browser)
    page.open()
    list_group_item = page.list_group_item()
    assert len(list_group_item) == COUNT_OF_LEFT_COLUMN_ITEMS

@allure.epic("Catalog page")
@allure.description("Checking visibility of list of groups")
def test_grid_view(browser):
    page = CatalogPage(browser)
    page.open()
    grid_view_button = page.grid_view()
    assert grid_view_button.is_displayed()

@allure.epic("Catalog page")
@allure.description("Checking visibility of navigation chain")
def test_nav_chain(browser):
    page = CatalogPage(browser)
    page.open()
    nav_chain = page.nav_chain()
    assert nav_chain.text == NAV_BAR_NAME

@allure.epic("Catalog page")
@allure.description("Checking is_enabled of sort by")
def test_select_sort_by(browser):
    page = CatalogPage(browser)
    page.open()
    select_sort_by = page.select_sort_by()
    assert select_sort_by.is_enabled()
