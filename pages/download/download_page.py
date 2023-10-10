from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


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


    def __init__(self, driver):
        super().__init__(driver)

    def click_sbis_plugin(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable(self.sbis_plugin))
        self.click(self.sbis_plugin)
