from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def __element(self, by, selector, index=0):
        return self.browser.find_elements(by, selector)[index]

    def _elements(self, by, selector):
        return self.browser.find_elements(by, selector)

    def _wait_for_visible(self, selector, index=0, wait=30):
        try:
            WebDriverWait(self.browser, wait).until(EC.visibility_of(self.__element(selector, index)))
        except:
            raise AssertionError("Selector not found")

    def _click(self, selector, index=0):
        self._wait_for_visible(selector, index)
        ActionChains(self.browser).move_to_element(self.__element(selector, index)).click().perform()

    def _send_keys(self, selector, index=0, *text):
        self._wait_for_visible(selector, index)
        ActionChains(self.browser).move_to_element(self.__element(selector, index)).click().send_keys(*text).perform()

    def _get_element_text(self, selector, index=0):
        return self.__element(selector, index).text
