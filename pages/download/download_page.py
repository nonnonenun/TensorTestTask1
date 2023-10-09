from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DownloadPage(BasePage):

    sbis_otchetnost = (By.XPATH, '//div[contains(@data-id,"ereport")]')
    sbis_plugin = (By.XPATH, '//div[contains(@data-id,"plugin")]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_sbis_plugin(self):
        self.click(self.sbis_plugin)
