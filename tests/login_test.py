import time
import unittest

from selenium import webdriver

from tests import CHROME_PATH


class BasicLogin(unittest.TestCase):

    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # Take locale browser and store into SELF
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser
        # browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # self.browser = browser

        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()

        time.sleep(1)



        #expected_url = 'http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList'
        #actual_url = browser.current_url
        #self.assertEqual(expected_url, actual_url)

        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)

    def test_empty_username(self):
        browser = self.browser

        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()

        time.sleep(1)

        username_message = browser.find_element_by_id('spanMessage').text

        self.assertEqual('Username cannot be empty', username_message)

    def test_empty_password(self):
        browser = self.browser

        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('btnLogin').click()

        time.sleep(1)

        password_message = browser.find_element_by_id('spanMessage').text

        self.assertEqual('Password cannot be empty', password_message)

    def test_wrong_password(self):
        browser = self.browser

        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('password1')
        browser.find_element_by_id('btnLogin').click()

        time.sleep(1)

        passw_wrong_message = browser.find_element_by_id('spanMessage').text

        self.assertEqual('Invalid credentials', passw_wrong_message)

    def test_wrong_username(self):
        browser = self.browser

        browser.get('http://hrm-online.portnov.com/')
        browser.find_element_by_id('txtUsername').send_keys('123errtt')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_id('btnLogin').click()

        time.sleep(1)

        passw_wrong_uname = browser.find_element_by_id('spanMessage').text

        self.assertEqual('Invalid credentials', passw_wrong_uname)



if __name__ == '__main__':
    unittest.main()
