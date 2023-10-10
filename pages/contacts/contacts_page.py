from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class ContactsPage(BasePage):

    tensor_banner = (By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]')
    current_region = By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_tensor_banner(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.tensor_banner))
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

    def get_partners_list(self):
        """
        Returns list of partner names for currently selected region
        example: for https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients it would be ['СБИС - Камчатка']
        """
        partner_webelements = self.find_elements(By.XPATH, '//div[starts-with(@class,"sbisru-Contacts-List__name")]')
        partners_list = []
        for partner_number in range(1, len(partner_webelements)+1):
            locator = (By.XPATH, f'(//div[starts-with(@class,"sbisru-Contacts-List__name")])[{partner_number}]')
            partner_name = self.get_text(locator)
            partners_list.append(partner_name)
        return partners_list

    def get_partners_city_list(self):
        """
        Returns list of cities for currently selected region where partner(s) exist(s)
        examples:
        for https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients it would be ['Петропавловск-Камчатский']
        for https://sbis.ru/contacts/77-moskva?tab=clients it would be ['Москва']
        """
        city_webelements = self.find_elements(By.XPATH, '//div[starts-with(@id, "city-id-")]')
        city_list = []

        if len(city_webelements) == 1:
            region = self.get_current_region()
            if region.startswith('г. '):
                region = region[3:]

            city_list.append(region)

        else:
            for city_number in range(2, len(city_webelements)+2):
                locator = (By.XPATH, f'//div[@id="city-id-{city_number}"]')
                partner_city = self.get_text(locator)
                city_list.append(partner_city)

        return city_list
