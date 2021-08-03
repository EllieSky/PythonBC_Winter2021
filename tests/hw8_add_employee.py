import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH


class AddEmployee(unittest.TestCase):
    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        browser.get('http://hrm-online.portnov.com/')
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        self.browser.find_element_by_id('btnLogin').click()

    def test_add_employee(self):
        # TO DO: clean and refactor code when have time
        # Set variables
        newEmpFirstName = 'Hanna2'
        newEmpLastName = 'Test'
        newEmpPassword = 'password'

        browser = self.browser
        url = browser.current_url
        self.login('admin', 'password')
        wait = WebDriverWait(browser, 10)

        # assert that EmployeeList window is loaded
        wait.until(expected_conditions.url_changes(url))
        self.assertTrue(browser.current_url.endswith('/pim/viewEmployeeList'))
        url = browser.current_url

        # T0DO: Wait till 'Add' button is visible and click. Why it doesn't work?
        # Second option. Use 'Add Employee' id='menu_pim_viewPimModule', click on link
        time.sleep(2)
        #wait.until(expected_conditions.visibility_of_element_located([By.ID, 'btnAdd']))
        #wait.until(expected_conditions.presence_of_element_located([By.ID, 'btnAdd']))
        #wait.until(expected_conditions.presence_of_element_located([By.ID, 'empsearch_job_title']))
        self.assertTrue(browser.find_element_by_id('btnAdd'))
        self.browser.find_element_by_id('btnAdd').click()

        # Wait and assert that AddEmployee window is loaded with all elements needed
        #time.sleep(5)
        wait.until(expected_conditions.url_changes(url))
        self.assertTrue(self.browser.current_url.endswith('/pim/addEmployee'))
        wait.until(expected_conditions.presence_of_element_located([By.ID, 'firstName']))
        wait.until(expected_conditions.presence_of_element_located([By.ID, 'lastName']))
        url = browser.current_url

        # Add values
        browser.find_element_by_id('firstName').send_keys(newEmpFirstName)
        browser.find_element_by_id('lastName').send_keys(newEmpLastName)

        # Save new employee id
        newEmpID = browser.find_element_by_id('employeeId').get_attribute('value')

        # Checkbox
        browser.find_element_by_id('chkLogin').click()

        # Wait until login info elements are visible
        #time.sleep(5)
        wait.until(expected_conditions.visibility_of_element_located([By.ID, 'user_name']))
        wait.until(expected_conditions.visibility_of_element_located([By.ID, 'user_password']))
        wait.until(expected_conditions.visibility_of_element_located([By.ID, 're_password']))

        # Add values to login details fields
        newEmpUserName = newEmpFirstName+newEmpLastName+newEmpID
        browser.find_element_by_id('user_name').send_keys(newEmpUserName)
        browser.find_element_by_id('user_password').send_keys(newEmpPassword)
        browser.find_element_by_id('re_password').send_keys(newEmpPassword)

        # Save new employee record
        browser.find_element_by_id('btnSave').click()

        # Wait and assert that viewPersonalDetails window is loaded with all elements needed
        #time.sleep(5)
        wait.until(expected_conditions.url_changes(url))
        #url = browser.current_url
        self.assertTrue(self.browser.current_url.endswith('/pim/viewPersonalDetails/empNumber/'+newEmpID))
        wait.until(expected_conditions.presence_of_element_located([By.ID, 'personal_txtEmpFirstName']))
        wait.until(expected_conditions.presence_of_element_located([By.ID, 'personal_txtEmpLastName']))

        # Assert that new employee record is saved
        newEmpFirstNameSaved = browser.find_element_by_id('personal_txtEmpFirstName').get_attribute('value')
        newEmpLastNameSaved = browser.find_element_by_id('personal_txtEmpLastName').get_attribute('value')
        newEmpIDNameSaved = browser.find_element_by_id('personal_txtEmployeeId').get_attribute('value')
        self.assertEqual(newEmpFirstNameSaved, newEmpFirstName)
        self.assertEqual(newEmpLastNameSaved, newEmpLastName)
        self.assertEqual(newEmpIDNameSaved, newEmpID)

        # logout
        browser.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/logout')

        # login as a new user
        self.login(newEmpUserName, newEmpPassword)
        # assert that EmployeeList window is loaded
        wait.until(expected_conditions.url_changes(url))
        wait.until(expected_conditions.presence_of_element_located([By.ID, "welcome"]))
        # Assert success
        self.assertTrue(browser.current_url.endswith('/pim/viewMyDetails'))
        welcome_message = browser.find_element_by_id('welcome').text
        self.assertEqual('Welcome '+newEmpFirstName, welcome_message)



if __name__ == '__main__':
    unittest.main()
