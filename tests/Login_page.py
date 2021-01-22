import time
import unittest

from selenium import webdriver

from fixtures.fixture import BaseFixture
from tests import CHROME_PATH


class BasicLogin(BaseFixture):



    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.driver
        self.login_page.login('admin', 'password')
        time.sleep(1)
        # assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)

    def test_empty_password(self):
        # Take browser out of SELF into local browser variable
        browser = self.driver

        self.login_page.login('admin', None)
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('http://hrm-online.portnov.com/symfony/web/index.php/auth/login', browser.current_url)
        self.assertEqual('Password cannot be empty', error_message)

    def test_empty_username(self):
        # Take browser out of SELF into local browser variable
        browser = self.driver

        self.login_page.login(None, None)
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('http://hrm-online.portnov.com/symfony/web/index.php/auth/login', browser.current_url)
        self.assertEqual('Username cannot be empty', error_message)

    def test_invalid_credentials_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.driver
        self.login_page.login('adminnn', 'passwordd')
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertTrue(browser.current_url.endswith('/auth/validateCredentials'))
        self.assertEqual('Invalid credentials', error_message)

if __name__ == '__main__':
    unittest.main()
