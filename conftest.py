import pytest
from selenium import webdriver


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
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

    if browser == "ie":
        driver = webdriver.Ie(executable_path="drivers/IEDriverServer.exe")

    if browser == "firefox":
        driver = webdriver.Firefox(executable_path="drivers/geckodriver.exe")

    if headless:
        driver.headless = True

    if maximized:
        driver.maximize_window()

    driver.get(url)
    driver.url = url

    def tear_down():
        driver.close()

    request.addfinalizer(tear_down)

    return driver
