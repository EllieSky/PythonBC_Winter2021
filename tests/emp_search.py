import time
import unittest
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import AdminLogin


class EmployeeInformationPage(object):
    def __init__(self, browser: Chrome):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def search_employees_by_job_title(self, job_title: str):
        Select(self.browser.find_element_by_id('empsearch_job_title')).select_by_visible_text(job_title)
        self.browser.find_element_by_id('searchBtn').click()
        self.wait.until(EC.presence_of_element_located(
            [By.XPATH, f'//select[@id="empsearch_job_title"]/option[@selected and text()="{job_title}"]']
        ))

    def get_job_title_from_resultTable_row(self, row=1):
        return self.browser.find_element_by_xpath(f'//*[@id="resultTable"]/tbody/tr[{row}]/td[5]').text

    def get_number_of_rows_from_resultTable(self):
        return len(self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr'))

    def get_all_job_titles_from_resultTable(self):
        return [el.text for el in self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')]


class EmpSearch(AdminLogin):

    def test_search_by_job_title(self):
        # self.browser.find_element_by_id('empsearch_job_title').send_keys('SDET')
        #  OR
        # self.browser.find_element_by_id('empsearch_job_title').click()
        # self.browser.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[9]').click()
        #  OR
        # Example of webdriver select
        emp_info = EmployeeInformationPage(self.browser)
        emp_info.search_employees_by_job_title('SDET')

        result = emp_info.get_job_title_from_resultTable_row()

        self.assertEqual('SDET', result)

        number_of_rows = emp_info.get_number_of_rows_from_resultTable()
        for i in range(number_of_rows):
            jtitle = emp_info.get_job_title_from_resultTable_row(i+1)
            self.assertEqual('SDET', jtitle)

        list_of_job_title_results = emp_info.get_all_job_titles_from_resultTable()
        result_set = set(list_of_job_title_results)

        self.assertEqual(1, len(result_set))
        self.assertEqual('SDET', result_set.pop())

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
