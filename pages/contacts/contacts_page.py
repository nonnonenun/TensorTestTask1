import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium import webdriver

from pages.base_page import BasePage

from selenium.webdriver.support.wait import WebDriverWait


class ContactsPage(BasePage):

    # locators
    tensor_banner = By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]'
    current_region = By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_tensor_banner(self):
        self.click(self.tensor_banner)
        return BasePage(self.driver)

    def click_region(self):
        self.click(self.current_region)
        from pages.regions_pop_up.regions_pop_up import RegionsPopUp
        return RegionsPopUp(self.driver)

    def get_current_region(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable(self.current_region))
        return self.get_text(self.current_region)
