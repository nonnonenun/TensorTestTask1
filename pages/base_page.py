import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def scroll(self):
        # self.driver.execute_script('window.scrollTo(0, window.innerHeight);')
        ActionChains(self.driver).scroll_by_amount(0, 200).perform()
        time.sleep(1)

    def move_to_element(self, locator):
        element = self.find(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def scroll_into_view(self, locator):
        element = self.find(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_sbis(self):
        element = self.find(By.XPATH, '//div[starts-with(@data-qa, "controls-Scroll")]')
        self.driver.execute_script("arguments[0].scrollTop=500;", element)

    def scroll_sbis_to_top(self):
        element = self.find(By.XPATH, '//div[starts-with(@data-qa, "controls-Scroll")]')
        self.driver.execute_script(f"arguments[0].scrollTo(0, 0);", element)

    def scroll_sbis_to_bottom(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        # javascript ne znayu
        # height = self.driver.execute_script('return document.evaluate("//div[starts-with(@data-qa, \'controls-Scroll\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollHeight;')
        element = self.find(By.XPATH, '//div[starts-with(@data-qa, "controls-Scroll")]')
        scroll_height = self.driver.execute_script('return document.getElementById("container").scrollHeight')
        # print(scroll_height)
        self.driver.execute_script(f'arguments[0].scrollTo(0, {scroll_height})', element)
