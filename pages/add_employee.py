from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage


class AddEmployeePage(BasePage):
    # def __init__(self, browser):
    #     super().__init__(browser)
    #     self.page_url = '/pim/addEmployee'
    #     self.page_header = 'Add Employee'

    @property
    def page_url(self):
        return '/pim/addEmployee'

    @property
    def page_header(self):
        return 'Add Employee'

    def fill_out_employee_form(self, first_name=None, last_name=None, emp_id=None, middle_name=None,
                               username=None, password=None, repeat_password=None):
        self.wait.until(
            EC.presence_of_element_located([By.ID, 'lastName'])
        ).send_keys(last_name) if last_name is not None else None
        self.wait.until(
            EC.presence_of_element_located([By.ID, 'firstName'])
        ).send_keys(first_name) if first_name is not None else None

        self.browser.find_element_by_id('middleName').send_keys(middle_name) if middle_name is not None else None

        if emp_id is not None:
            self.browser.find_element_by_id('employeeId').clear()
            self.browser.find_element_by_id('employeeId').send_keys(emp_id)

        if username or password or repeat_password:
            self.browser.find_element_by_id('chkLogin').click()
            self.wait.until(EC.visibility_of_element_located(
                [By.ID, 'user_name']
            )).send_keys(username)

            self.browser.find_element_by_id('user_password').send_keys(password) if password is not None else None
            if repeat_password is not None:
                self.browser.find_element_by_id('re_password').send_keys(repeat_password)

    def get_employee_id(self):
        return self.browser.find_element_by_id('employeeId').get_attribute('value')

    def save(self):
        self.browser.find_element_by_id('btnSave').click()