from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage
from tests import DEFAULT_ADMIN_PASSWORD


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = '/auth/login'
        self.page_header = 'LOGIN Panel'

    def login(self, username='admin', password=DEFAULT_ADMIN_PASSWORD):
        url = self.browser.current_url
        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        self.browser.find_element_by_id('btnLogin').click()
        self.wait.until(EC.url_changes(url)) if username and password else None
