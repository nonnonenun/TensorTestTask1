import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# from selenium import webdriver


from pages.base_page import BasePage
from utilities.locators import LocatorsHeader


class PageHeader(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def click_home():
        pass

    def click_kontakti(self):
        kontakti = LocatorsHeader.kontakti
        self.click(kontakti)
        from pages.contacts.contacts_page import ContactsPage
        return ContactsPage(self.driver)

    @staticmethod
    def click_podderzhka():
        pass

    @staticmethod
    def click_nachat_rabotu():
        pass
