from abc import abstractmethod, ABC

from selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from tests import BASE_URL


class BasePage(ABC, Base):

    # def __init__(self, browser):
    #     super().__init__(browser)
    #     # self.page_url = ''
    #     # self.page_header = ''

    @property
    @abstractmethod
    def page_url(self):
        return ''

    @property
    @abstractmethod
    def page_header(self):
        return ''

    def wait_for_page_to_load(self):
        self.wait.until(EC.url_contains(self.page_url))

    def get_page_header(self):
        return self.browser.find_element_by_css_selector('.head>h1').text

    def go_to_page(self):
        self.browser.get(BASE_URL + self.page_url)
