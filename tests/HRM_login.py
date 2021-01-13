import unittest

import time
#import selenium webdriver

from selenium import webdriver


class BasicLogin(unittest.TestCase):
    def test_valid_login(self):
        #browser session
        browser = webdriver.Chrome(executable_path='/Users/hannamazur/Projects/PythonBC_Winter2021/chromedriver')
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


if __name__ == '__main__':
    unittest.main()
