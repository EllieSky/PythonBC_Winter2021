import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixture.fixture import BaseFixture
from pages.login import LoginPage
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

    def f_l_name(self, f_name, l_name):
        # enter first name
        self.browser.find_element_by_id('firstName').send_keys(f_name) if f_name else None

        if l_name:
            # enter lastname
            self.browser.find_element_by_id('lastName').send_keys(l_name)

    def test_add_emp(self):
        self.login_page.login()

        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located(
                [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))

        self.browser.find_element_by_id('btnAdd').click()

        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located([By.ID, 'lastName']))
        # wait.until(expected_conditions.url_contains('/addEmployee'))

        self.f_l_name('Kateryna', 'Germash')


        self.browser.find_element_by_id('firstName').send_keys('kateryna')
        self.browser.find_element_by_id('lastName').send_keys('Germash')

        emp_id = self.browser.find_element_by_id('employeeId').get_attribute('value')

        self.browser.find_element_by_id('chkLogin').click()

        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located([By.ID, 'user_name'])
        )

        # send keys immediately
        self.browser.find_element_by_id('user_name').send_keys(
            'Kateryna', 'Germash', emp_id)
        self.browser.find_element_by_id('user_password').send_keys('password')
        self.browser.find_element_by_id('re_password').send_keys('password')
        self.browser.find_element_by_id('btnSave').click()

        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located(
                [By.XPATH, '//a[contains(text(),"Personal Details")]'])
        )
        f_name = self.browser.find_element_by_id('personal_txtEmpFirstName').get_attribute('value')
        l_name = self.browser.find_element_by_id('personal_txtEmpLastName').get_attribute('value')
        self.assertTrue(f_name, 'Kateryna')
        self.assertTrue(l_name, 'Germash')

        self.browser.find_element_by_id('welcome').click()

        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(
                [By.XPATH, '//a[contains(text(),"Logout")]']
            )
        )

        self.browser.find_element_by_xpath('//a[contains(text(),"Logout")]').click()

        url = self.browser.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        self.assertTrue(self.browser.current_url, url)

        # WebDriverWait(self.browser, 5).until(
        #     expected_conditions.url_contains('/auth/login')
        # )

        # WebDriverWait(self.browser, 5).until(
        #     expected_conditions.presence_of_element_located(
        #         [By.ID, 'txtUsername'])
        # )

        self.login('KaterynaGermash3338', 'password')

        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located(
                [By.XPATH, '//h1[contains(text(),"Personal Details")]']
            )
        )
        welcome_user = self.browser.find_element_by_id('welcome').text
        self.assertTrue('Welcome Kateryna', welcome_user)

        # time.sleep(3)




if __name__ == '__main__':
    unittest.main()
