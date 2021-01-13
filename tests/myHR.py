import unittest
import time

from selenium import webdriver
from tests import CHROME_PATH

class BasicLogin(unittest.TestCase):
    def tearDown(self) -> None:
        self.browser.quit()

    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser = browser

    def test_valid_login(self):
        # Take local browser and store it into SELF
        browser = self.browser

        # browser session
        # browser = webdriver.Chrome(executable_path="/drivers/chromedriver.exe")
        browser = webdriver.Chrome(executable_path=CHROME_PATH)

        # open the URL
        browser.get('http://hrm-online.portnov.com/')

        # enter username
        browser.find_element_by_id('txtUsername').send_keys('admin')

        # enter password
        browser.find_element_by_id('txtPassword').send_keys('password')

        # click login button
        browser.find_element_by_id('btnLogin').click()

        time.sleep(1)

        # assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)

        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
