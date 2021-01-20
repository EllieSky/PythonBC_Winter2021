import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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

        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located(
                [By.CSS_SELECTOR, '#empsearch_job_title > option[selected][value="42"]']))

        # time.sleep(2)

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]').text
        self.assertEqual('SDET', result)

        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')

        for item in list_of_web_elements_jtitles:
            self.assertEqual('SDET', item.text)

    def test_search_by_id(self):
        emp_id = '3250'

        self.login('admin', 'password')
        self.browser.find_element_by_id('empsearch_id').send_keys(emp_id)

        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        list_of_rows = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr')
        # self.assertTrue(len(list_of_rows) == 1)
        # OR
        self.assertEqual(1, len(list_of_rows))


        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[2]').text
        self.assertEqual(emp_id, result)

    def test_search_by_emp_name(self):
        name = "amb"

        self.login('admin', 'password')
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(name)
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(Keys.ESCAPE)

        self.assertFalse(self.browser.find_element_by_class_name('ac_results').is_displayed())

        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        list_of_rows = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr')

        for single_row in list_of_rows:
            first_name = single_row.find_elements_by_xpath(".//td[3]").text.lower()
            last_name = single_row.find_elements_by_xpath(".//td[4]").text.lower()

            self.assertIn(name, [first_name, last_name])
            # OR
            self.assertTrue(first_name.find(name) != -1 or last_name.find(name) != -1)

        for index in range(len(list_of_rows)):
            first_name = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[' + (index + 1) + ']/td[3]').text
            last_name = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[' + (index + 1) + ']/td[4]').text

            self.assertTrue(name in first_name + last_name)



if __name__ == '__main__':
    unittest.main()
