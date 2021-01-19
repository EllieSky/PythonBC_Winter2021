import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from tests import CHROME_PATH


class Login(unittest.TestCase):

    def setUp(self) -> None:
        # browser session creating for Chrome
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        # Take locale browser and store into SELF
        self.browser = browser
        browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        # enter username
        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            # enter password
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        self.browser.find_element_by_id('btnLogin').click()

    def test_search_by_job_title(self):
        # Take browser out of SELF into local browser variable
        # browser = self.browser
        self.login('admin', 'password')
        time.sleep(1)
        self.browser.find_element_by_id('empsearch_job_title').send_keys('SDET')

        # OR

        # self.browser.find_element_by_id('empsearch_job_title').click()
        # self.browser.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[9]').click()

        # OR

        # Example of webdriver select

        # Select(self.browser.find_element_by_id('empsearch_job_title')).select_by_visible_text('SDET')

        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]').text
        self.assertEqual('SDET', result)

        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')

        for item in list_of_web_elements_jtitles:
            self.assertEqual('SDET', item.text)

    def test_search_by_id(self):
        self.login('admin', 'password')
        time.sleep(1)
        self.browser.find_element_by_id('empsearch_id').send_keys('3250')


        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[2]').text
        self.assertEqual('3250', result)

        list_of_web_elements_jids = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[2]')

        for item in list_of_web_elements_jids:
            self.assertEqual(len(list_of_web_elements_jids), 1)

    def test_search_by_name(self):
        self.login('admin', 'password')
        time.sleep(1)
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys('David')
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(Keys.ESCAPE)


        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]').text
        self.assertEqual('David', result)

        list_of_web_elements_name = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]')

        for item in list_of_web_elements_name:
            self.assertEqual('David', item.text)

    def test_search_by_name2(self):
        self.login('admin', 'password')
        time.sleep(1)
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys('amb')
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(Keys.ESCAPE)


        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        result_l_n = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[4]').text
        result_f_n = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]').text
        self.assertIn('amb', (result_l_n or result_f_n))

        # list_of_web_elements_name = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]')

        # for item in list_of_web_elements_name:
        #    self.assertEqual('David', item.text)



if __name__ == '__main__':
    unittest.main()
