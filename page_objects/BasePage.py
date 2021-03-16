import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def __element(self, by, selector, index=0):
        element = None
        try:
            element = self.browser.find_elements(by, selector)[index]
            logging.info(f"__element: {by} {selector} {index}")
        except Exception as err:
            logging.error(f"__element: {by} {selector} {index}" + str(err))
        return element

    def _elements(self, by, selector):
        elements = None
        try:
            elements = self.browser.find_elements(by, selector)
            logging.info(f"_elements: {by} {selector}")
        except Exception as err:
            logging.error(f"_elements: {by} {selector}" + str(err))
        return elements

    def _wait_for_element_visible(self, selector, index=0, wait=60):
        try:
            element = WebDriverWait(self.browser, wait).until(EC.visibility_of(self.__element(selector, index)))
            logging.info(f"_wait_for_element_visible: {selector} {index}")
        except:
            logging.error(f"_wait_for_element_visible: {selector} {index}")
            raise AssertionError()
        return element

    def _click(self, selector, index=0):
        self._wait_for_element_visible(selector, index)
        try:
            ActionChains(self.browser).move_to_element(self.__element(selector, index)).click().perform()
            logging.info(f"_click: {selector} {index}")
        except Exception as err:
            logging.error(f"_click: {selector} {index}" + str(err))

    def _send_keys(self, selector, index=0, *text):
        self._wait_for_element_visible(selector, index)
        try:
            ActionChains(self.browser).move_to_element(self.__element(selector, index)).click().send_keys(
                *text).perform()
            logging.info(f"_send_keys: {selector} {index} {text}")
        except Exception as err:
            logging.error(f"_send_keys: {selector} {index} {text}" + str(err))

    def _get_element_text(self, selector, index=0):
        elem_text = None
        try:
            elem_text = self.__element(selector, index).text
            logging.info(f"_get_element_text: {selector} {index}")
        except Exception as err:
            logging.error(f"_get_element_text: {selector} {index}" + str(err))
        return elem_text

    def _open(self, url):
        open_url = None
        try:
            open_url = self.browser.get(url)
            logging.info(f"_open: {url}")
        except Exception as err:
            logging.error(f"_open: {url}" + str(err))
        return open_url