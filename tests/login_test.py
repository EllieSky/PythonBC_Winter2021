import unittest

from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from fixtures.fixture import BaseFixture

class BasicLogin(BaseFixture):
    @unittest.skip
    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser
        url = browser.current_url
        self.login_page.login()

        self.long_wait.until(expected_conditions.url_changes(url))
        self.wait.until(expected_conditions.presence_of_element_located([By.ID, "welcome"]))
        # assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)

    @parameterized.expand([
        ('empty_password', 'admin', None, '/auth/login', 'Password cannot be empty'),
        ('empty_username', None, None, '/auth/login', 'Username cannot be empty'),
        ('invalid_credentials', 'adminnn', 'passwordd', '/auth/validateCredentials', 'Invalid credentials')
    ])
    def test_invalid_login(self, test_name, username, password, partial_url, expected_error_msg):
        browser = self.browser
        self.login_page.login(username, password)
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertTrue(browser.current_url.endswith(partial_url))
        self.assertEqual(expected_error_msg, error_message)

    # def test_empty_password(self):
    #     # Take browser out of SELF into local browser variable
    #     browser = self.browser
    #
    #     # self.login_page.login('admin', None)
    #     # OR
    #     self.login_page.login(password=None)
    #     error_message = browser.find_element_by_id('spanMessage').text
    #     self.assertEqual('http://hrm-online.portnov.com/symfony/web/index.php/auth/login', browser.current_url)
    #     self.assertEqual('Password cannot be empty', error_message)
    #
    # def test_empty_username(self):
    #     # Take browser out of SELF into local browser variable
    #     browser = self.browser
    #
    #     self.login_page.login(None, None)
    #     error_message = browser.find_element_by_id('spanMessage').text
    #     self.assertEqual('http://hrm-online.portnov.com/symfony/web/index.php/auth/login', browser.current_url)
    #     self.assertEqual('Username cannot be empty', error_message)
    #
    # def test_invalid_credentials_login(self):
    #     # Take browser out of SELF into local browser variable
    #     browser = self.browser
    #     self.login_page.login('adminnn', 'passwordd')
    #     error_message = browser.find_element_by_id('spanMessage').text
    #     self.assertTrue(browser.current_url.endswith('/auth/validateCredentials'))
    #     self.assertEqual('Invalid credentials', error_message)

if __name__ == '__main__':
    unittest.main()
