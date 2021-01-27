import unittest
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login import LoginPage
from tests import CHROME_PATH, PROJ_DIR


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        driver.get("http://hrm-online.portnov.com/")
        self.login_page = LoginPage(driver)
        self.login_page.login()

    def tearDown(self) -> None:
        if self._outcome.errors[1][1]: # Checks is test Failed, and only then takes screenshot
            test_results_folder = f"{PROJ_DIR}/screenshots" # Screenshot folder location
            if not os.path.exists(test_results_folder): # If condition to create screenshot folde only if it does not exist
                os.mkdir(test_results_folder)
            test_name = self._testMethodName  # Assigning the test name to the screenshot below
            self.driver.save_screenshot(f"{test_results_folder}/{test_name}.png")  # Taking a screenshot with a test name


            file = open(f"{test_results_folder}/{test_name}.html", "w", encoding="utf-8")
            file.write(self.driver.page_source)
            file.close()

            # Or WITH can be used so we don't have to use file.close() See below!

            # with open(f"{test_results_folder}/{test_name}.html", "w", encoding="utf-8") as file:
            #     file.write(self.driver.page_source)


        self.driver.quit()

class AdminLoginFixture(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()
