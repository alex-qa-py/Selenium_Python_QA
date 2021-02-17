from page_objects.ProductPage import ProductPage

URL = "index.php?route=product/product&path=57&product_id=49"
PRODUCT_ID = "49"
TITLES = ["Your Store", "Samsung Galaxy Tab 10.1"]
COUNT_OF_IMAGES = 7
ATTRIBUTES = ["title", "value"]


def test_images_additional(browser):
    browser.open(URL)
    list_of_images = ProductPage(browser).images_additional()
    assert len(list_of_images) == COUNT_OF_IMAGES


def test_product_title(browser):
    browser.open(URL)
    product_title = ProductPage(browser).product_title()
    assert product_title[0].get_attribute(ATTRIBUTES[0]) == TITLES[1]


def test_button_card(browser):
    browser.open(URL)
    button_card = ProductPage(browser).button_card()
    assert button_card.is_displayed()


def test_input_quantity(browser):
    browser.open(URL)
    product_id = ProductPage(browser).input_quantity()
    assert product_id.is_displayed()


def test_titles(browser):
    browser.open(URL)
    h1 = ProductPage(browser).titles()
    assert h1[0].text == TITLES[0]
    assert h1[1].text == TITLES[1]
