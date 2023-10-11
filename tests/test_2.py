from pages.components.page_header import PageHeader
from tests.base_test import BaseTest
import time     # there's a delay in region change


class TestRegionChange(BaseTest):

    def test_region_change(self):
        header = PageHeader(self.driver)
        contacts_page = header.click_kontakti()
        initial_region = contacts_page.get_current_region()
        assert initial_region != 'Камчатский край'
        initial_partners = contacts_page.get_partners_list()
        assert initial_partners != ['СБИС - Камчатка']

        regions_pop_up = contacts_page.click_region()
        regions_pop_up.select_region('Камчатский край')

        time.sleep(1)   # there's a delay in region change

        url = contacts_page.get_url()
        assert url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        title = contacts_page.get_title()
        assert title == 'СБИС Контакты — Камчатский край'
        currently_selected_region = contacts_page.get_current_region()
        assert 'Камчатский край' in currently_selected_region

        kamchatka_partners = contacts_page.get_partners_list()
        assert kamchatka_partners == ['СБИС - Камчатка']
