import time
import unittest

from selenium import webdriver

from tests import CHROME_PATH


class BasicLogIn(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        browser=self.browser

        browser.get('http://hrm-online.portnov.com')

        browser.find_element_by_id("txtUsername").send_keys("admin")

        browser.find_element_by_id("txtPassword").send_keys("password")

        browser.find_element_by_id("btnLogin").click()
        time.sleep(3)

        self.assertTrue(browser.current_url.endswith("pim/viewEmployeeList"))
        welcome_message=browser.find_element_by_id("welcome").text

        self.assertEqual("Welcome Admin", welcome_message)


if __name__ == '__main__':
    unittest.main()
