import time
import unittest

from selenium import webdriver

from tests import CHROME_PATH


class BasicLogIn(unittest.TestCase):
    def setUp(self) -> None:
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser = browser
        browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        if username:
            self.browser.find_element_by_id("txtUsername").send_keys(username) if username else  None
        if password:
            self.browser.find_element_by_id("txtPassword").send_keys(password)

        self.browser.find_element_by_id("btnLogin").click()


    def test_valid_login(self):
        browser=self.browser
        self.login("admin", "password")
        time.sleep(3)

        self.assertTrue(browser.current_url.endswith("pim/viewEmployeeList"))
        welcome_message=browser.find_element_by_id("welcome").text
        self.assertEqual("Welcome Admin", welcome_message)

    def test_invalid_login(self):
        browser = self.browser
        self.login("jbkjh", "knlkn")
        time.sleep(1)

        spanMessage = browser.find_element_by_id('spanMessage').text
        self.assertEqual("Invalid credentials", spanMessage)

    def test_empty_password_login(self):
        browser = self.browser
        self.login("admin", None)

        time.sleep(3)

        failing_massege = browser.find_element_by_id('spanMessage').text
        self.assertEqual("Password cannot be empty", failing_massege)


if __name__ == '__main__':
    unittest.main()
