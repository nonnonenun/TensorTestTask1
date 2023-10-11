from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DownloadPage(BasePage):

    # left menu
    sbis_otchetnost = (By.XPATH, '//div[contains(@data-id,"ereport")]')
    sbis_plugin = (By.XPATH, '//div[contains(@data-id,"plugin")]')
    sbis_roznica = (By.XPATH, '//div[contains(@data-id,"retail")]')
    sbis_presto = (By.XPATH, '//div[contains(@data-id,"presto")]')
    sbis_kiosk = (By.XPATH, '//div[contains(@data-id,"kiosk")]')
    sbis_arhiv = (By.XPATH, '//div[contains(@data-id,"archive")]')
    dlya_1c = (By.XPATH, '//div[contains(@data-id,"1c")]')
    udalenniy_pomoshnik = (By.XPATH, '//div[contains(@data-id,"support")]')
    sertifikati_ep = (By.XPATH, '//div[contains(@data-id,"certificates")]')
    sredstva_kriptozashiti = (By.XPATH, '//div[contains(@data-id,"crypto")]')

    # locator for downloading
    web_installer_dowload_link = (By.XPATH, '(//h3[contains(text(),"Веб-установщик")]/../..)//a')

    def __init__(self, driver):
        super().__init__(driver)

    def click_sbis_plugin(self):
        self.click(self.sbis_plugin)

    def click_download_web_installer(self):
        self.click(self.web_installer_dowload_link)

    def get_web_installer_download_link(self):
        pass

    @property
    def get_web_installer_download_link_text(self):
        return self.get_text(self.web_installer_dowload_link)

    def get_web_installer_size(self) -> float:
        text = self.get_web_installer_download_link_text
        size_string = text[13:-4]
        size = float(size_string)
        return size
