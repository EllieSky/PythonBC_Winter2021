import time
import unittest

from selenium import webdriver


class BasicLogin(unittest.TestCase):
    def test_valid_login(self):
        browser = webdriver.Chrome(executable_path='C:/Users/aspir/Automation/Python_BC_Winter_2021/chromedriver.exe')
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










if __name__ == '__main__':
    unittest.main()
