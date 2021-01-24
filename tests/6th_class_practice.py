import time
import unittest

from selenium import webdriver


class BasicLogIn(unittest.TestCase):
    def test_valid_login(self):
        browser = webdriver.Chrome(executable_path="/drivers/chromedriver.exe")


        browser.get('http://hrm-online.portnov.com')

        browser.find_element_by_id("txtUsername").send_keys("admin")

        browser.find_element_by_id("txtPassword").send_keys("password")

        browser.find_element_by_id("btnLogin").click()
        time.sleep(1)

        self.assertTrue(browser.current_url.endswith("pim/viewEmployeeList"))
        welcome_message=browser.find_element_by_id("welcome").text

        self.assertEqual("Welcome Admin", welcome_message)


if __name__ == '__main__':
    unittest.main()
