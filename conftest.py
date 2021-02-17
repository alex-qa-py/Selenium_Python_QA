import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "ie"])
    parser.addoption("--url", action="store", default="http://localhost/opencart/")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--url")

    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    if browser == "ie":
        driver = webdriver.Ie(IEDriverManager().install())

    if browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())

    if headless:
        driver.headless = True

    if maximized:
        driver.maximize_window()

    def open(path=""):
        return driver.get(url + path)

    driver.open = open

    def tear_down():
        driver.close()

    request.addfinalizer(tear_down)

    return driver
