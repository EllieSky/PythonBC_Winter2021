import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import AdminLogin


class EmpSearch(AdminLogin):
    def setUp(self) -> None:
        super().setUp()
        self.wait = WebDriverWait(self.browser, 5)
        self.wait.until(EC.presence_of_element_located(
            [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']
        ))

    def test_search_by_job_title(self):
        # self.browser.find_element_by_id('empsearch_job_title').send_keys('SDET')
        #  OR
        # self.browser.find_element_by_id('empsearch_job_title').click()
        # self.browser.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[9]').click()
        #  OR
        # Example of webdriver select
        Select(self.browser.find_element_by_id('empsearch_job_title')).select_by_visible_text('SDET')
        self.browser.find_element_by_id('searchBtn').click()

        self.wait.until(EC.presence_of_element_located(
            [By.CSS_SELECTOR, '#empsearch_job_title > option[selected][value="42"]']
        ))

        # time.sleep(2)

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]').text
        self.assertEqual('SDET', result)

        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')

        for item in list_of_web_elements_jtitles:
            self.assertEqual('SDET', item.text)

    def test_search_by_id(self):
        emp_id = '3250'

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

        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(name)
        self.browser.find_element_by_id('empsearch_employee_name_empName').send_keys(Keys.ESCAPE)

        self.assertFalse(self.browser.find_element_by_class_name('ac_results').is_displayed())

        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(2)

        list_of_rows = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr')

        for single_row in list_of_rows:
            first_name = single_row.find_element_by_xpath(".//td[3]").text.lower()
            last_name = single_row.find_element_by_xpath(".//td[4]").text.lower()

            self.assertIn(name, " ".join([first_name, last_name]))
            # OR
            self.assertTrue(first_name.find(name) != -1 or last_name.find(name) != -1,
                            f"Neither the first name ({first_name}) nor the last name ({last_name}) matched the search criteria: {name}")

        for index in range(len(list_of_rows)):
            first_name = self.browser.find_element_by_xpath(
                '//*[@id="resultTable"]/tbody/tr[' + str(index + 1) + ']/td[3]').text.lower()
            last_name = self.browser.find_element_by_xpath(
                '//*[@id="resultTable"]/tbody/tr[' + str(index + 1) + ']/td[4]').text.lower()

            self.assertTrue(name in first_name + last_name, f"Full name '{first_name} {last_name}' did not match the search keyword '{name}'.")



if __name__ == '__main__':
    unittest.main()
