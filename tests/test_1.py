# "error":"element click intercepted" in firefox browser without time.sleep() before clicks, works in chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config import TestData
from pages.base_page import BasePage
from pages.components.page_header import PageHeader
from pages.home.home_page import HomePage
from pages.contacts.contacts_page import ContactsPage
from tests.base_test import BaseTest


class TestTask1Tensor(BaseTest):

    def test_task_1_tensor(self):
        home_page = HomePage(self.driver)
        header = PageHeader(self.driver)
        title = home_page.get_title()
        assert title == TestData.SBIS_HOME_TITLE

        contacts_page = header.click_kontakti()

        title = contacts_page.get_title()
        assert title[:13] == TestData.SBIS_CONTACTS_TITLE

        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(ContactsPage.tensor_banner))
        tensor_home = contacts_page.click_tensor_banner()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        wait.until(EC.title_is(TestData.TENSOR_HOME_TITLE))

        url = tensor_home.get_url()
        assert url == TestData.TENSOR_HOME_URL
        title = tensor_home.get_title()
        assert title == TestData.TENSOR_HOME_TITLE

        blok_sila = (By.XPATH, '//div[starts-with(@class,"tensor_ru-Index__block4-content")]')
        blok_sila_title = (By.XPATH, '//div[starts-with(@class,"tensor_ru-Index__block4-content")]//p[contains(@class,"title")]')
        blok_sila_podrobnee = (By.XPATH, '//div[starts-with(@class,"tensor_ru-Index__block4-content")]//a[text()="Подробнее"]')

        tensor_home.scroll_into_view(blok_sila)

        assert tensor_home.get_text(blok_sila_title) == 'Сила в людях'

        wait.until(EC.visibility_of_element_located(blok_sila_podrobnee))
        wait.until(EC.element_to_be_clickable(blok_sila_podrobnee))
        tensor_home.click(blok_sila_podrobnee)

        tensor_about = BasePage(self.driver)

        wait.until(EC.title_is(TestData.TENSOR_ABOUT_TITLE))

        url = tensor_about.get_url()
        assert url == TestData.TENSOR_ABOUT_URL
        title = tensor_about.get_title()
        assert title == TestData.TENSOR_ABOUT_TITLE

        blok_rabotaem = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')
        wait.until(EC.presence_of_element_located(blok_rabotaem))
        tensor_about.scroll_into_view(blok_rabotaem)

        wait.until(EC.visibility_of_element_located(blok_rabotaem))

        blok_rabotaem_fotki_xpath = '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img'
        vse_foto_bloka_rabotaem = tensor_about.find_elements(By.XPATH, blok_rabotaem_fotki_xpath)

        for foto in vse_foto_bloka_rabotaem:
            assert foto.size == vse_foto_bloka_rabotaem[0].size
