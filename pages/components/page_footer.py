from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.download.download_page import DownloadPage


class PageFooter(BasePage):

    skachat_sbis = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[10]/ul/li[6]/a')

    def __init__(self, driver):
        super().__init__(driver)

    def click_skachat_sbis(self):
        self.click(self.skachat_sbis)
        return DownloadPage(self.driver)
