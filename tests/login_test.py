import time
import unittest

from selenium import webdriver


class BasicLogin(unittest.TestCase):
    def test_valid_login(self):
        # browser session
        browser = webdriver.Chrome(executable_path='/Users/ellie/Automation/PythonBC_Winter2021/chromedriver')
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


if __name__ == '__main__':
    unittest.main()
