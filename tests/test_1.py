# import pytest

# from config.config import TestData
from selenium.webdriver.common.by import By
from selenium import webdriver
from config.config import TestData
from pages.base_page import BasePage
from pages.components.page_header import PageHeader
from pages.contacts.contacts_page import ContactsPage
from pages.home.home_page import HomePage
from tests.base_test import BaseTest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class TestHome(BaseTest):

    def test_home(self):
        # self.driver.get(TestData.NOT_BASE_URL)
        home_page = HomePage(self.driver)
        header = PageHeader(self.driver)
        title = home_page.get_title()
        assert title == TestData.SBIS_HOME_TITLE

        contacts_page = header.click_kontakti()

        title = contacts_page.get_title()
        assert title[:13] == TestData.SBIS_CONTACTS_TITLE

        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1

        tensor_home = contacts_page.click_tensor_banner()

        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        url = tensor_home.get_url()
        assert url == TestData.TENSOR_HOME_URL
        title = tensor_home.get_title()
        assert title == TestData.TENSOR_HOME_TITLE

        blok_sila = (By.XPATH, '//div[starts-with(@class,"tensor_ru-Index__block4-content")]')
        blok_sila_title = (By.XPATH, '//div[starts-with(@class,"tensor_ru-Index__block4-content")]//p[contains(@class,"title")]')
        blok_sila_podrobnee = (By.XPATH, '//div[starts-with(@class,"tensor_ru-Index__block4-content")]//a[text()="Подробнее"]')

        tensor_home.scroll_into_view(blok_sila)
        assert tensor_home.get_text(blok_sila_title) == 'Сила в людях'

        tensor_home.click(blok_sila_podrobnee)

        tensor_about = BasePage(self.driver)
        url = tensor_about.get_url()
        assert url == TestData.TENSOR_ABOUT_URL
        title = tensor_about.get_title()
        assert title == TestData.TENSOR_ABOUT_TITLE

        blok_rabotaem = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')
        tensor_about.scroll_into_view(blok_rabotaem)

        # fotki_elements_list = tensor_about.find_elements(By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img') # tak rabotaet no dlinno

        # blok_rabotaem_fotki = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img') # tak ne rabotaet
        #fotki_elements_list = tensor_about.find_elements(blok_rabotaem_fotki) # tak ne rabotaet

        blok_rabotaem_fotki_xpath = '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img'
        vse_foto_bloka_rabotaem = tensor_about.find_elements(By.XPATH, blok_rabotaem_fotki_xpath)

        razmeri_foto = []
        for foto in vse_foto_bloka_rabotaem:
            razmeri_foto.append(foto.size)
            assert foto.size == vse_foto_bloka_rabotaem[0].size

        print(razmeri_foto)

        # assert razmeri_foto[0] == razmeri_foto[1] == razmeri_foto[2] == razmeri_foto[3]
        # assert all(foto == razmeri_foto[0] for foto in razmeri_foto)
        # print(all(foto == razmeri_foto[0] for foto in razmeri_foto))
