import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver


class BasePage:
    """
    The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
    """
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click() # DRY principle - Dont Repeat Yourself

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
