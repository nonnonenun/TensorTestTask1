import time

from pages.components.page_footer import PageFooter
from tests.base_test import BaseTest


class TestDownloadPlugin(BaseTest):

    def test_download_plugin(self):
        footer = PageFooter(self.driver)
        footer.scroll_sbis_to_bottom()
        download_page = footer.click_skachat_sbis()
        time.sleep(2)
        download_page.click_sbis_plugin()
        time.sleep(5)
