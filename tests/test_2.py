import time

from pages.components.page_header import PageHeader
from pages.home.home_page import HomePage
from tests.base_test import BaseTest
from selenium import webdriver


class TestRegionChange(BaseTest):

    def test_region_change(self):

        header = PageHeader(self.driver)

        contacts_page = header.click_kontakti()

        currently_selected_region = contacts_page.get_current_region()
        my_original_location = 'Севастополь'
        assert my_original_location in currently_selected_region

        regions_pop_up = contacts_page.click_region()

        regions_pop_up_header = regions_pop_up.pop_up_get_header_text()

        assert regions_pop_up_header == 'Выберите свой регион'

        regions_pop_up.select_region('Камчатский край')

        time.sleep(1)

        url = contacts_page.get_url()
        assert url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        title = contacts_page.get_title()
        assert title == 'СБИС Контакты — Камчатский край'
        currently_selected_region = contacts_page.get_current_region()
        assert 'Камчатский край' in currently_selected_region
