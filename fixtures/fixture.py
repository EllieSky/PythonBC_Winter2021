import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from menues.user_menu import UserMenu
from pages.add_employee import AddEmployeePage
from pages.employee_info import EmployeeInformationPage
from pages.login import LoginPage
from tests import CHROME_PATH, DEFAULT_WAIT, LONG_WAIT, OUTPUT_DIR


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        # browser session

        if os.environ.get('JOB_NAME'):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            browser = webdriver.Chrome(executable_path=CHROME_PATH, options=chrome_options)
        else:
            browser = webdriver.Chrome(executable_path=CHROME_PATH)

        self.browser = browser
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
        self.long_wait = WebDriverWait(self.browser, LONG_WAIT)
        self.login_page = LoginPage(browser)

        # optional design choice:
        self.user_menu = UserMenu(self.browser)
        self.pim_page = EmployeeInformationPage(self.browser)
        self.add_emp_page = AddEmployeePage(self.browser)

        # browser.get(f'http://{DOMAIN}')
        # OR
        self.login_page.go_to_page()

    def tearDown(self) -> None:
        if self._outcome.errors[1][1]:
            test_results_folder = OUTPUT_DIR
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
        self.wait.until(
            EC.presence_of_element_located(
                [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']
            ))
