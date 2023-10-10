from pages.base_page import BasePage
from utilities.locators import LocatorsHeader


class PageHeader(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_home(self):
        pass

    def click_kontakti(self):
        kontakti = LocatorsHeader.kontakti
        self.click(kontakti)
        from pages.contacts.contacts_page import ContactsPage
        return ContactsPage(self.driver)

    def click_podderzhka(self):
        pass

    def click_nachat_rabotu(self):
        pass
