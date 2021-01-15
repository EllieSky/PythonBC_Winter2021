import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from tests import CHROME_PATH


class EmpSearch(unittest.TestCase):
    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        self.browser.find_element_by_id('btnLogin').click()

    def test_search_by_job_title(self):
        self.login('admin', 'password')
        # self.browser.find_element_by_id('empsearch_job_title').send_keys('SDET')
        #  OR
        # self.browser.find_element_by_id('empsearch_job_title').click()
        # self.browser.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[9]').click()
        #  OR
        # Example of webdriver select
        Select(self.browser.find_element_by_id('empsearch_job_title')).select_by_visible_text('SDET')
        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]').text
        self.assertEqual('SDET', result)

        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')

        for item in list_of_web_elements_jtitles:
            self.assertEqual('SDET', item.text)
    def test_search_by_employee_id(self):
        self.login('admin', 'password')
        self.browser.find_element_by_id('empsearch_id').send_keys('635919')
        self.browser.find_element_by_id('searchBtn').click()
        actual_search_result = self.browser.find_element_by_link_text('635919').text
        print('result' +  actual_search_result)
        self.assertTrue('635919' == actual_search_result)
        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')
      #  print("lenght of list is " + str(len(list_of_web_elements_jtitles)))
        self.assertTrue(len(list_of_web_elements_jtitles)==1)
    def test_send_esc_key(self):
        self.login('admin','password')
        time.sleep(1)
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys('David')
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(Keys.ESCAPE)
        self.browser.find_element_by_id('searchBtn').click()
        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]')
        for item in list_of_web_elements_jtitles:
            self.assertEqual('David', item.text)
            print("text david" + item.text)
        time.sleep(4)


if __name__ == '__main__':
    unittest.main()
