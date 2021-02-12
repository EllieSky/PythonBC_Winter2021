from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from base.base_page import BasePage


class EmployeeInfoType:
    ID = 2
    FIRST_MIDDLE_NAME = 3
    LAST_NAME = 4
    JOB_TITLE = 5
    EMPLOYMENT_STATUS = 6
    SUB_UNIT = 7
    SUPERVISOR = 8


class EmployeeInformationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = '/pim/viewEmployeeList'
        self.page_header = 'Employee Information'

    def search_employees_by_job_title(self, job_title: str):
        Select(self.browser.find_element_by_id('empsearch_job_title')).select_by_visible_text(job_title)
        self.browser.find_element_by_id('searchBtn').click()
        self.wait.until(EC.presence_of_element_located(
            [By.XPATH, f'//select[@id="empsearch_job_title"]/option[@selected and text()="{job_title}"]']
        ))

    def search_employees_by_employee_id(self, emp_id):
        self.browser.find_element_by_id('empsearch_id').send_keys(emp_id)
        self.browser.find_element_by_id('searchBtn').click()
        self.wait.until(EC.presence_of_element_located(
            [By.CSS_SELECTOR, "#empsearch_id[value='3250']"]
        ))

    def get_job_title_from_resultTable_row(self, row=1):
        return self.get_info_from_resultTable_row(EmployeeInfoType.JOB_TITLE, row)

    def get_employee_id_from_resultTable_row(self, row=1):
        return self.get_info_from_resultTable_row(EmployeeInfoType.ID, row)

    def get_info_from_resultTable_row(self, info, row=1):
        return self.browser.find_element_by_xpath(f'//*[@id="resultTable"]/tbody/tr[{row}]/td[{info}]').text

    def get_number_of_rows_from_resultTable(self):
        return len(self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr'))

    def get_all_job_titles_from_resultTable(self):
        return [el.text for el in self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')]


