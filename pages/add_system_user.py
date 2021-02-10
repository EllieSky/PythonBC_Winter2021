from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddSystemUserPage(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

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