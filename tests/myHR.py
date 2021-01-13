import unittest

from selenium import webdriver


class BasicLogin(unittest.TestCase):
    def test_valid_login(self):
        # browser session
        browser = webdriver.Chrome(executable_path="C:/Users/rxdai/portnov computer school/PCS-Python-Silver-BC/Automation/PythonBC_Winter2021/chromedriver.exe")

        # open the URL
        browser.get('http://hrm-online.portnov.com/')

        # enter username
        browser.find_element_by_id('txtUsername').send_keys('admin')

        # enter password
        browser.find_element_by_id('txtPassword').send_keys('password')

        # click login button
        browser.find_element_by_id('btnLogin').click()
        # browser.find_element_by_id('btnLogin').send_keys('login')

        # assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        welcome_message = browser.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', welcome_message)


        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
