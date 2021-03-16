import logging

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.1.69")
    parser.addoption("--bversion", action="store", default="88.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger()
    fhandler = logging.FileHandler(filename='app.log', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.INFO)

    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        }
    }

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities,
        options=chrome_options)

    def tear_down():
        driver.close()

    request.addfinalizer(tear_down)

    return driver
