import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import BaseFixture


class AddEmployee(BaseFixture):
    def test_add_employee_with_credentials(self):
        wait = WebDriverWait(self.browser, 5)
        first = "Jane"
        last = "Doe"

        self.login_page.login()
        wait.until(EC.url_contains('/pim/viewEmployeeList'))
        wait.until(
            EC.presence_of_element_located(
                [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']
            ))
        self.browser.find_element_by_id('btnAdd').click()
        wait.until(EC.url_contains('/pim/addEmployee'))

        wait.until(
            EC.presence_of_element_located([By.ID, 'lastName'])).send_keys(last)
        wait.until(
            EC.presence_of_element_located([By.ID, 'firstName'])).send_keys(first)

        emp_id = self.browser.find_element_by_id('employeeId').get_attribute('value')

        self.browser.find_element_by_id('chkLogin').click()
        wait.until(EC.visibility_of_element_located(
            [By.ID, 'user_name']
        # )).send_keys("JaneDoe" + emp_id)
        # )).send_keys(f"JaneDoe{emp_id}")
        )).send_keys(first, last, emp_id)

        self.browser.find_element_by_id('user_password').send_keys('password')
        self.browser.find_element_by_id('re_password').send_keys('password')

        self.browser.find_element_by_id('btnSave').click()

        wait.until(EC.url_contains('/empNumber/' + emp_id))

        self.browser.find_element_by_id("welcome").click()

        wait.until(EC.visibility_of_element_located(
            [By.LINK_TEXT, "Logout"]
        )).click()

        wait.until(EC.url_contains('/auth/login'))

        # self.login(first + last + emp_id, 'password')
        self.login_page.login((first, last, emp_id))

        welcome_message = wait.until(EC.presence_of_element_located(
            [By.ID, 'welcome']
        )).text

        self.assertEqual(f"Welcome {first}", welcome_message)


if __name__ == '__main__':
    unittest.main()
