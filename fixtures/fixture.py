import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login import LoginPage
from tests import CHROME_PATH


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        driver.get("http://hrm-online.portnov.com/")
        self.login_page = LoginPage(driver)
        self.login_page.login()

    def tearDown(self) -> None:
        self.driver.quit()

class AdminLoginFixture(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()
        wait =  WebDriverWait