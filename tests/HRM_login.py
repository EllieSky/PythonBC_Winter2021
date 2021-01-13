import unittest

import time
#import selenium webdriver

from selenium import webdriver

from tests import CHROME_PATH


class BasicLogin(unittest.TestCase):
    def setUp(self) -> None:
        #browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # Take browser out of local browser variable into SELF
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser
        #open the URL
        browser.get('http://hrm-online.portnov.com/')
        #enter username
        browser.find_element_by_id('txtUsername').send_keys('admin')
        #enter password
        browser.find_element_by_id('txtPassword').send_keys('password')
        #click login button
        browser.find_element_by_id('btnLogin').click()
        #assert success
        time.sleep(1)
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_message)
        self.assertTrue(browser.find_element_by_id('welcome').is_displayed())


    def test_empty_user_name_valid_password(self):
        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()
        time.sleep(1)
        self.assertTrue(browser.current_url.endswith('/auth/login'))
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('Username cannot be empty', error_message)

    def test_empty_password_valid_username(self):
        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('')
        browser.find_element_by_id('btnLogin').click()
        time.sleep(1)
        self.assertTrue(browser.current_url.endswith('/auth/login'))
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('Password cannot be empty', error_message)

    def test_empty_password_empty_username(self):
        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('')
        browser.find_element_by_id('txtPassword').send_keys('')
        browser.find_element_by_id('btnLogin').click()
        time.sleep(1)
        self.assertTrue(browser.current_url.endswith('/auth/login'))
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('Username cannot be empty', error_message)

    def test_valid_username_invalid_password(self):
        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('qwerty')
        browser.find_element_by_id('btnLogin').click()
        time.sleep(1)
        self.assertTrue(browser.current_url.endswith('/auth/validateCredentials'))
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('Invalid credentials', error_message)

    def test_invalid_user_name_invalid_password(self):
        browser = self.browser
        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('test')
        browser.find_element_by_id('txtPassword').send_keys('test')
        browser.find_element_by_id('btnLogin').click()
        time.sleep(1)
        self.assertTrue(browser.current_url.endswith('/auth/validateCredentials'))
        error_message = browser.find_element_by_id('spanMessage').text
        self.assertEqual('Invalid credentials', error_message)


if __name__ == '__main__':
    unittest.main()
