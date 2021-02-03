import time
import unittest
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import AdminLoginFixture


class EmployeeInformationPage(object):
    def __init__(self, browser: Chrome):
        self.driver = browser
        self.wait = WebDriverWait(browser, 5)

    def search_employees_by_job_title(self, job_title: str):
        self.driver.find_element_by_id('menu_admin_viewAdminModule').click()
        self.wait.until(EC.element_to_be_clickable([By.ID, "menu_admin_viewAdminModule"]))
        self.driver.find_element_by_id("btnAdd").click()
        time.sleep(25)

#     def get_job_title_from_resultTable_row(self, row=1):
#         return self.driver.find_element_by_xpath(f'//*[@id="resultTable"]/tbody/tr[{row}]/td[5]').text
#
#     def get_number_of_rows_from_resultTable(self):
#         return len(self.driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr'))
#
#     def get_all_job_titles_from_resultTable(self):
#         return [el.text for el in self.driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')]
#
#
# class EmpSearch(AdminLogin):
#
#     def test_search_by_job_title(self):
#         # self.browser.find_element_by_id('empsearch_job_title').send_keys('SDET')
#         #  OR
#         # self.browser.find_element_by_id('empsearch_job_title').click()
#         # self.browser.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[9]').click()
#         #  OR
#         # Example of webdriver select
#         emp_info = EmployeeInformationPage(self.browser)
#         emp_info.search_employees_by_job_title('SDET')
#
#         result = emp_info.get_job_title_from_resultTable_row()
#
        # self.assertEqual('SDET', result)
#
#         number_of_rows = emp_info.get_number_of_rows_from_resultTable()
#         for i in range(number_of_rows):
#             jtitle = emp_info.get_job_title_from_resultTable_row(i+1)
#             self.assertEqual('SDET', jtitle)
#
#         list_of_job_title_results = emp_info.get_all_job_titles_from_resultTable()
#         result_set = set(list_of_job_title_results)
#
#         self.assertEqual(1, len(result_set))
#         self.assertEqual('SDET', result_set.pop())