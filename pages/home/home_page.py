from pages.base_page import BasePage
# from pages.components import page_header
from pages.components.page_header import PageHeader


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_page_title(self):
        title = self.get_title()
        return title
