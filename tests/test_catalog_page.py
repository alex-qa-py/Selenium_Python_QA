from page_objects.CatalogPage import CatalogPage

URL = "/index.php?route=product/category&path=20"
PRODUCT_COUNT = 12
COUNT_OF_LEFT_COLUMN_ITEMS = 10
NAV_BAR_NAME = "Desktops"


def test_product_count(browser):
    browser.open(URL)
    list_of_products = CatalogPage(browser).list_of_products()
    assert len(list_of_products) == PRODUCT_COUNT


def test_list_group_item(browser):
    browser.open(URL)
    list_group_item = CatalogPage(browser).list_group_item()
    assert len(list_group_item) == COUNT_OF_LEFT_COLUMN_ITEMS


def test_grid_view(browser):
    browser.open(URL)
    grid_view_button = CatalogPage(browser).grid_view()
    assert grid_view_button.is_displayed()


def test_nav_chain(browser):
    browser.open(URL)
    nav_chain = CatalogPage(browser).nav_chain()
    assert nav_chain.text == NAV_BAR_NAME


def test_select_sort_by(browser):
    browser.open(URL)
    select_sort_by = CatalogPage(browser).select_sort_by()
    assert select_sort_by.is_enabled()
