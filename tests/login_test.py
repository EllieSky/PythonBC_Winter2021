import time
import unittest

from selenium import webdriver

from tests import CHROME_PATH


class BasicLogin(unittest.TestCase):

    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # Take  local browser and store it into SELF
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser

        # open the URL
        browser.get("http://hrm-online.portnov.com/")

        # enter username
        browser.find_element_by_id("txtUsername").send_keys("admin")

        # enter password
        browser.find_element_by_id("txtPassword").send_keys("password")

        # click Login button
        browser.find_element_by_id("btnLogin").click()

        # assert success
        time.sleep(1)
        expected_url = "http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList"
        actual_url = browser.current_url
        self.assertEqual(expected_url, actual_url)
        self.assertIn("viewEmployeeList", actual_url)

        # or use 2nd assert success
        self.assertTrue(browser.current_url.endswith("/pim/viewEmployeeList"))
        welcome_message = browser.find_element_by_id("welcome").text
        self.assertEqual("Welcome Admin", welcome_message)

    def test_empty_username(self):
        browser = self.browser
        browser.get("http://hrm-online.portnov.com/")
        browser.find_element_by_id("btnLogin").click()
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Username cannot be empty", error_message)
        print("User can not login with empty username")

    def test_empty_password(self):
        browser = self.browser
        browser.get("http://hrm-online.portnov.com/")
        browser.find_element_by_id("txtUsername").send_keys("admin")
        browser.find_element_by_id("btnLogin").click()
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Password cannot be empty", error_message)
        print("User can not login with empty password")

    def test_wrong_password(self):
        browser = self.browser
        browser.get("http://hrm-online.portnov.com/")
        browser.find_element_by_id("txtUsername").send_keys("admin")
        browser.find_element_by_id("txtPassword").send_keys("passwordd")
        browser.find_element_by_id("btnLogin").click()
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_message)
        print("User can not login with wrong password")


    def test_wrong_username(self):
        browser = self.browser
        browser.get("http://hrm-online.portnov.com/")
        browser.find_element_by_id("txtUsername").send_keys("aaddmmin")
        browser.find_element_by_id("txtPassword").send_keys("password")
        browser.find_element_by_id("btnLogin").click()
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_message)
        print("User can not login with wrong username")





if __name__ == '__main__':
    unittest.main()
