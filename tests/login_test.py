import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH


class BasicLogin(unittest.TestCase):

    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # Take  local browser and store it into SELF
        self.browser = browser
        browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        # enter username
        self.browser.find_element_by_id("txtUsername").send_keys(username) if username else None

        if password:
            # enter password
            self.browser.find_element_by_id("txtPassword").send_keys(password)

        # example of conditional assignment
        # gender = 'boy'
        # greeting = "Ms." if gender == 'Female' else "Mr."

        # click Login button
        self.browser.find_element_by_id("btnLogin").click()

    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser

        # open the URL
        # browser.get("http://hrm-online.portnov.com/")

        # enter username
        # browser.find_element_by_id("txtUsername").send_keys("admin")

        # enter password
        # browser.find_element_by_id("txtPassword").send_keys("password")

        # click Login button
        # browser.find_element_by_id("btnLogin").click()
        url = browser.current_url

        self.login("admin", "password")

        # assert success
        time.sleep(1)

        wait = WebDriverWait(browser, 15)

        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))
        wait.until(expected_conditions.url_changes(url))
        wait.until(expected_conditions.presence_of_element_located([By.ID, "welcome"]))

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
        # browser.get("http://hrm-online.portnov.com/")
        # browser.find_element_by_id("btnLogin").click()
        self.login(None, None)
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Username cannot be empty", error_message)
        print("User can not login with empty username")

    def test_empty_password(self):
        browser = self.browser
        # browser.get("http://hrm-online.portnov.com/")
        # browser.find_element_by_id("txtUsername").send_keys("admin")
        # browser.find_element_by_id("btnLogin").click()
        self.login("admin", None)
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Password cannot be empty", error_message)
        print("User can not login with empty password")

    def test_wrong_password(self):
        browser = self.browser
        # browser.get("http://hrm-online.portnov.com/")
        # browser.find_element_by_id("txtUsername").send_keys("admin")
        # browser.find_element_by_id("txtPassword").send_keys("passwordd")
        # browser.find_element_by_id("btnLogin").click()
        self.login("admin", "passwordd")
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_message)
        print("User can not login with wrong password")

    def test_wrong_username(self):
        browser = self.browser
        # browser.get("http://hrm-online.portnov.com/")
        # browser.find_element_by_id("txtUsername").send_keys("aaddmmin")
        # browser.find_element_by_id("txtPassword").send_keys("password")
        # browser.find_element_by_id("btnLogin").click()
        self.login("addmmmin", "password")
        error_message = browser.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_message)
        print("User can not login with wrong username")


if __name__ == '__main__':
    unittest.main()