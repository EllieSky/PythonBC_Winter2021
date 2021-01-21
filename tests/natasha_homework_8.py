import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH

from selenium import webdriver


class Homework_8(unittest.TestCase):
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

    def send_keys_to_field(self, selector, text):
        self.browser.find_element_by_id(selector).send_keys(text)

    def button_click(self, selector):
        self.browser.find_element_by_id(selector).click()

    def enter_employee_ID(self, id):
        self.browser.find_element_by_id('empsearch_id').send_keys(id)

    def enter_employee_name(self, name):
        el = self.browser.find_element_by_id('empsearch_employee_name_empName')
        el.send_keys(name)
        el.send_keys(Keys.ESCAPE)

    def test_search_by_employee_ID(self):
        self.login('admin', 'password')
        time.sleep(1)

        # self.browser.find_element_by_xpath("//input[@id='btnAdd']").click()
        self.button_click("btnAdd")

        wait = WebDriverWait(self.browser, 15)
        wait.until(expected_conditions.url_contains("/pim/addEmployee"))

        self.send_keys_to_field("firstName", "John")
        self.send_keys_to_field("lastName", "Test")

        employee_id = self.browser.find_element_by_id("employeeId").get_attribute("value")
        print("Employee ID: " + employee_id)
        time.sleep(1)

        self.button_click("chkLogin")

        self.send_keys_to_field("user_name", ("John", "Test", employee_id))

        self.send_keys_to_field("user_password", ("Test", employee_id))
        self.send_keys_to_field("re_password", ("Test", employee_id))
        self.button_click("btnSave")

        wait.until(expected_conditions.url_contains("/pim/viewPersonalDetails/empNumber/" + employee_id))
        self.assertTrue(self.browser.find_element_by_class_name('personalDetails').is_displayed())
        self.assertEqual(self.browser.find_element_by_id("personal_txtEmpFirstName").get_attribute("value"), "John")

        action = ActionChains(self.browser)
        self.browser.find_element_by_id("welcome").click()
        action.move_to_element(self.browser.find_element_by_xpath("//a[contains(text(),'Logout')]")).perform()
        self.browser.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

        self.login(("John", "Test", employee_id), ("Test", employee_id))

        self.assertTrue(self.browser.current_url.endswith("/pim/viewMyDetails"))
        welcome_message = self.browser.find_element_by_id("welcome").text
        self.assertEqual("Welcome John", welcome_message)


if __name__ == '__main__':
    unittest.main()
