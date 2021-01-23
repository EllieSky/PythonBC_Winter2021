import unittest

from selenium import webdriver

from pages.login import LoginPage
from tests import CHROME_PATH


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser
        self.login_page = LoginPage(browser)

    def tearDown(self) -> None:
        self.browser.quit()


class AdminLogin(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()
