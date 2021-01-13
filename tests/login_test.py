import time
import unittest

from selenium import webdriver

from tests import CHROME_PATH


class BasicLogin(unittest.TestCase):

    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # Take local browser and store it into SELF
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        # Take browser out of SELF into local browser variable
        browser = self.browser

        # open the URL
        browser.get('http://hrm-online.portnov.com/')
        # enter username
        browser.find_element_by_id('txtUsername').send_keys('admin')
        # enter password
        browser.find_element_by_id('txtPassword').send_keys('password')
        # click Login button
        browser.find_element_by_id('btnLogin').click()
        time.sleep(1)
        # assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)

    def test_empty_password(self):
        # Put your code here
        pass


if __name__ == '__main__':
    unittest.main()
