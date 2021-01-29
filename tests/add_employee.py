import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import BaseFixture
from pages.login_page import LoginPage
from tests import CHROME_PATH


class AddEmployee(BaseFixture):

    # def login(self, username, password):
    #     # enter username
    #     self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None
    #
    #     if password:
    #         # enter password
    #         self.browser.find_element_by_id('txtPassword').send_keys(password)
    #
    #     self.browser.find_element_by_id('btnLogin').click()

    def test_add_emp(self):
        wait = WebDriverWait(self.browser, 5)
        first = 'Kateryna'
        last = 'Germash'

        self.login_page.login('admin', 'password')

        wait.until(EC.url_contains('/pim/viewEmployeeList'))

        wait.until(EC.presence_of_element_located(
                [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))

        self.browser.find_element_by_id('btnAdd').click()

        wait.until(EC.url_contains('/pim/addEmployee'))

        wait.until(
             EC.presence_of_element_located([By.ID, 'lastName'])).send_keys(last)

        wait.until(
            EC.presence_of_element_located([By.ID, 'firstName'])).send_keys(first)

        emp_id = self.browser.find_element_by_id('employeeId').get_attribute('value')

        self.browser.find_element_by_id('chkLogin').click()

        wait.until(
            EC.visibility_of_element_located([By.ID, 'user_name'])
        # ).send_keys(f'KaterynaGermash{emp_id}')
        ).send_keys(first, last, emp_id)


        # send keys immediately
        # self.browser.find_element_by_id('user_name').send_keys(
        #     'Kateryna', 'Germash', emp_id)
        self.browser.find_element_by_id('user_password').send_keys('password')
        self.browser.find_element_by_id('re_password').send_keys('password')
        self.browser.find_element_by_id('btnSave').click()

        wait.until(EC.url_contains('/empNumber/' + emp_id))

        # wait.until(
        #     EC.presence_of_element_located(
        #         [By.XPATH, '//a[contains(text(),"Personal Details")]'])
        # )
        #
        # f_name = self.browser.find_element_by_id('personal_txtEmpFirstName').get_attribute('value')
        # l_name = self.browser.find_element_by_id('personal_txtEmpLastName').get_attribute('value')
        # self.assertTrue(f_name, 'Kateryna')
        # self.assertTrue(l_name, 'Germash')

        self.browser.find_element_by_link_text('Job').click()

        wait.until(EC.visibility_of_element_located([By.CSS_SELECTOR, 'h2']))
        self.browser.find_element_by_xpath('//input[@id="btnSave"]').click()
        self.browser.find_element_by_id('job_job_title').send_keys('QA Engineer')
        self.browser.find_element_by_id('job_emp_status').send_keys('Full Time')
        self.browser.find_element_by_id('btnSave').click()

        wait.until(EC.presence_of_element_located(
            [By.CSS_SELECTOR, '#job_job_title > option[selected][value = "46"]']))

        self.browser.find_element_by_link_text('Welcome Admin').click()

        wait.until(
             EC.visibility_of_element_located(
                 [By.LINK_TEXT, 'Logout']))
        self.browser.find_element_by_link_text('Logout').click()

        wait.until(EC.url_contains('/auth/login'))

        self.login_page.login((first, last, emp_id), 'password')

        wait.until(EC.url_contains('/pim/viewEmployeeList'))

        welcome_message = wait.until(
             EC.presence_of_element_located([By.ID, 'welcome'])).text

        self.assertEqual(f'Welcome {first}', welcome_message)



        # welcome_user = self.browser.find_element_by_id('welcome').text
        # self.assertTrue('Welcome Kateryna', welcome_user)

        # time.sleep(3)




if __name__ == '__main__':
    unittest.main()
