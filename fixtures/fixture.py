import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from tests import CHROME_PATH


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser = browser
        browser.get('http://hrm-online.portnov.com/')
        self.login_page = LoginPage(browser)
        # self.login_page.login()

    def tearDown(self) -> None:
        self.browser.quit()


class AdminLogin(BaseFixture):

    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()


