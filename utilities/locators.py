from selenium.webdriver.common.by import By


class LocatorsHeader:
    sbis_header_logo = (By.XPATH, '')
    tarifi = (By.XPATH, r'//ul[starts-with(@class, "sbisru-Header__menu")]//a[text()="Тарифы"]')
    kontakti = (By.XPATH, r'//ul[starts-with(@class, "sbisru-Header__menu")]//a[text()="Контакты"]')
    podderzhka = (By.XPATH, r'//ul[starts-with(@class, "sbisru-Header__menu")]//a[text()="Поддержка"]')
    nachat_rabotu = (By.XPATH, '')

class LocatorsContacts:
    tensor_banner = (By.XPATH, r'//a[@class="sbisru-Contacts__logo-tensor mb-12"]')

class LocatorsTensorHeader:
    o_kompanii = (By.XPATH, r'//ul[@name="headerMenu"]//a[text()="О компании"]')
