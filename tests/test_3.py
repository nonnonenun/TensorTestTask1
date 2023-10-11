from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.components.page_footer import PageFooter
from pages.download.download_page import DownloadPage
from tests.base_test import BaseTest
import os
import send2trash
import time

# СКАЧИВАНИЕ В ПАПКУ С ПРОЕКТОМ НЕ РЕАЛИЗОВАНО!

# try downloading via requests or headless mode or configure relative download path(if this is even possible for chrome)


class TestDownloadPlugin(BaseTest):

    def test_download_plugin(self):
        footer = PageFooter(self.driver)
        footer.scroll_sbis_to_bottom()
        download_page = footer.click_skachat_sbis()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable(DownloadPage.sbis_plugin))
        download_page.click_sbis_plugin()

        expected_web_installer_size = download_page.get_web_installer_size()

        wait.until(EC.element_to_be_clickable(DownloadPage.web_installer_dowload_link))
        download_page.click_download_web_installer()

        path_to_file = r'C:\Download\sbisplugin-setup-web.exe'

        time_to_wait = 20
        time_counter = 0

        while not os.path.exists(path_to_file):
            time.sleep(1)
            time_counter += 1
            if time_counter > time_to_wait:
                break

        if os.path.isfile(path_to_file):
            file_size = os.path.getsize(path_to_file)
        else:
            raise ValueError(f"{path_to_file} isn't a file!")

        file_size_in_mb_rounded = round(file_size/1024/1024, 2)

        assert file_size_in_mb_rounded == expected_web_installer_size

        send2trash.send2trash(r'C:\Download\sbisplugin-setup-web.exe')
