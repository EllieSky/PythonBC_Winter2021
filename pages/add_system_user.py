from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage


class AddSystemUserPage(BasePage):
    # def __init__(self, browser):
    #     super().__init__(browser)
    #     self.page_url = '/admin/saveSystemUser'
    #     self.page_header = 'Add User'

    @property
    def page_url(self):
        return '/admin/saveSystemUser'

    @property
    def page_header(self):
        return 'Add User'

    def wait_for_page_to_load(self):
        super().wait_for_page_to_load()
        self.wait.until(EC.presence_of_element_located((By.ID, 'systemUser-information')))

    def fill_out_user_form(self, emp_name=None, username=None, password=None, repeat_password=None):
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'systemUser_employeeName_empName'))).send_keys(emp_name) if emp_name is not None else None
        self.browser.find_element_by_id(
            'systemUser_userName').send_keys(username) if username is not None else None
        self.browser.find_element_by_id('systemUser_password').send_keys(password) if password is not None else None

        if repeat_password is not None:
            self.browser.find_element_by_id('systemUser_confirmPassword').send_keys(repeat_password)

    def save(self):
        self.browser.find_element_by_id('btnSave').click()