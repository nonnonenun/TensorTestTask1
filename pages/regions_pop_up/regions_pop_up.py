# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegionsPopUp(BasePage):

    pop_up_header = (By.XPATH, '//div[@class="sbis_ru-Region-Panel__header-text"]//span')
    pop_up_closer = (By.XPATH, '//div[@class="sbis_ru-Region-Panel__header-close"]')

    def __init__(self, driver):
        super().__init__(driver)

    def pop_up_get_header_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.pop_up_header))
        return self.get_text(self.pop_up_header)

    def pop_up_close(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.pop_up_header))
        self.click(self.pop_up_closer)

    def select_region(self, region: str):
        region_to_be_clicked = (By.XPATH,
                                f'//ul[@class="sbis_ru-Region-Panel__list"]//li/span[contains(text(),"{region}")]')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(region_to_be_clicked))
        self.click(region_to_be_clicked)
        # time.sleep(1)
