import allure

from page_objects.ProductPage import ProductPage
PRODUCT_ID = "49"
TITLES = ["Your Store", "Samsung Galaxy Tab 10.1"]
COUNT_OF_IMAGES = 7
ATTRIBUTES = ["title", "value"]

@allure.epic("Product page")
@allure.description("Checking count of additional images")
def test_images_additional(browser):
    page = ProductPage(browser)
    page.open()
    list_of_images = page.images_additional()
    assert len(list_of_images) == COUNT_OF_IMAGES

@allure.epic("Product page")
@allure.description("Checking attribute title of image")
def test_product_title(browser):
    page = ProductPage(browser)
    page.open()
    product_title = page.product_title()
    assert product_title[0].get_attribute(ATTRIBUTES[0]) == TITLES[1]

@allure.epic("Product page")
@allure.description("Checking is_displayed of card button")
def test_button_card(browser):
    page = ProductPage(browser)
    page.open()
    button_card = page.button_card()
    assert button_card.is_displayed()

@allure.epic("Product page")
@allure.description("Checking is_displayed of quantity input")
def test_input_quantity(browser):
    page = ProductPage(browser)
    page.open()
    product_id = page.input_quantity()
    assert product_id.is_displayed()

@allure.epic("Product page")
@allure.description("Checking title of tag h1")
def test_titles(browser):
    page = ProductPage(browser)
    page.open()
    h1 = page.titles()
    assert h1[0].text == TITLES[0]
    assert h1[1].text == TITLES[1]
