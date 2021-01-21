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
        # Take local browser and store it into SELF
        self.browser = browser
        # open the URL
        browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        # enter username
        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            # enter password
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        # example of conditional assignment
        # gender = 'Female'
        # greeting = "Ms." if gender == 'Female' else "Mr."

        # click Login button
        self.browser.find_element_by_id('btnLogin').click()


    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser
        url = browser.current_url
        self.login('admin', 'password')
        wait = WebDriverWait(browser, 15)

        wait.until(expected_conditions.url_changes(url))
        wait.until(expected_conditions.presence_of_element_located([By.ID, "welcome"]))
        # assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)

    def test_empty_password(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser

        self.login('admin', None)
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('http://hrm-online.portnov.com/symfony/web/index.php/auth/login', browser.current_url)
        self.assertEqual('Password cannot be empty', error_message)

    def test_empty_username(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser

        self.login(None, None)
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('http://hrm-online.portnov.com/symfony/web/index.php/auth/login', browser.current_url)
        self.assertEqual('Username cannot be empty', error_message)

    def test_invalid_credentials_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser
        self.login('adminnn', 'passwordd')
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertTrue(browser.current_url.endswith('/auth/validateCredentials'))
        self.assertEqual('Invalid credentials', error_message)

if __name__ == '__main__':
    unittest.main()
