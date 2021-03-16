import allure

import helper

TITLE = "Your Store"

@allure.feature("UI testing")
@allure.step("Check title")
def test_title(browser):
    browser.get(f"{helper.get_test_env()}/opencart/")
    assert TITLE in browser.title
