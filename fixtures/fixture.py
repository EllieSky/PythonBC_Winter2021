import unittest
import os

from selenium import webdriver

from pages.login import LoginPage
from tests import CHROME_PATH, PROJ_PATH


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        browser.get("http://hrm-online.portnov.com/")
        # Take  local browser and store it into SELF
        self.browser = browser
        self.login_page = LoginPage(browser)

    def tearDown(self) -> None:
        if self._outcome.errors[1][1]:
            test_results_folder = f"{PROJ_PATH}/screenshots"
            if not os.path.exists(test_results_folder):
                os.mkdir(test_results_folder)
            test_name = self._testMethodName
            self.browser.save_screenshot(f"{test_results_folder}/{test_name}.png")

            file = open(f"{test_results_folder}/{test_name}.html", 'w', encoding="utf-8")
            file.write(self.browser.page_source)
            file.close()

            # with open(f"{test_results_folder}/{test_name}.html", 'w', encoding="utf-8") as file:
            #     file.write(self.browser.page_source)

        self.browser.quit()


class AdminLogin(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()
