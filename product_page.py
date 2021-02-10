from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


URL = "/index.php?route=product/product&path=57&product_id=49"
IMAGE = ".thumbnail"
CARD_BUTTON = "#button-cart"
PRODUCT_ID_SELECTOR = "product_id"
PRODUCT_ID = "49"
TITLES_TEG = "h1"
TITLES = ["Your Store", "Samsung Galaxy Tab 10.1"]
COUNT_OF_IMAGES = 7
ATTRIBUTES = ["title", "value"]


def test_images_additional(browser):
    browser.get(browser.url + URL)
    list_of_images = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, IMAGE)))
    assert len(list_of_images) == COUNT_OF_IMAGES


def test_product_title(browser):
    browser.get(browser.url + URL)
    product_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, IMAGE)))
    assert product_title.get_attribute(ATTRIBUTES[0]) == TITLES[1]


def test_button_card(browser):
    browser.get(browser.url + URL)
    button_card = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, CARD_BUTTON)))
    assert button_card.is_displayed


def test_product_id(browser):
    browser.get(browser.url + URL)
    product_id = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.NAME, PRODUCT_ID)))
    assert product_id.get_attribute(ATTRIBUTES[1]) == PRODUCT_ID


def test_titles(browser):
    browser.get(browser.url + URL)
    h1 = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
        (By.TAG_NAME, TITLES_TEG)))
    assert h1[0].text == TITLES[0]
    assert h1[1].text == TITLES[1]

