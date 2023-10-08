import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

from config.config import WebDriverExecutablesPaths, TestData

from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    web_driver = None
    if request.param == 'chrome':
        service = Service(WebDriverExecutablesPaths.CHROME_EXECUTABLE_PATH)
        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(service=service, options=options)
    if request.param == 'firefox':
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    # web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL)
    # web_driver.get('https://tensor.ru/')
    yield
    web_driver.close()