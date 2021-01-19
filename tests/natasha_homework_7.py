import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from tests import CHROME_PATH


class Homework_7(unittest.TestCase):
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

    def enter_employee_ID(self, id):
        self.browser.find_element_by_id('empsearch_id').send_keys(id)

    def enter_employee_name(self, name):
        el = self.browser.find_element_by_id('empsearch_employee_name_empName')
        el.send_keys(name)
        el.send_keys(Keys.ESCAPE)

    def test_search_by_employee_ID(self):
        self.login('admin', 'password')
        time.sleep(1)
        self.enter_employee_ID("441915")

        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(1)

        result = self.browser.find_element_by_xpath('//tbody/tr[1]/td[2]').text
        self.assertEqual('441915', result)

        list_of_web_elements_IDs = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')
        qty = len(list_of_web_elements_IDs)
        print("Qty of records found: " + str(qty))
        self.assertEqual(1, qty)

    def test_search_by_employee_name(self):
        self.login('admin', 'password')
        time.sleep(1)
        self.enter_employee_name("David")
        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(1)

        list_of_web_elements_employee_names = self.browser.find_elements_by_xpath("//tbody/tr/td[3]")

        count = 0
        for item in list_of_web_elements_employee_names:
            if item.text.find('David') != -1:
                count = count + 1

        self.assertEqual(count, len(list_of_web_elements_employee_names), "Not all entries contain David")

    def test_search_by_employee_partial_name(self):
        self.login('admin', 'password')
        time.sleep(1)
        self.enter_employee_name("amb")
        self.browser.find_element_by_id('searchBtn').click()

        time.sleep(1)

        list_of_web_elements_employee_names = self.browser.find_elements_by_xpath("//tbody/tr/td[3]")
        list_of_web_elements_employee_last_names = self.browser.find_elements_by_xpath("//tbody/tr/td[4]")

        count = 0
        for i in range(len(list_of_web_elements_employee_names)):
            if list_of_web_elements_employee_last_names[i].text.lower().find('amb') != -1 or \
               list_of_web_elements_employee_names[i].text.lower().find('amb') != -1:
                count = count+1

        self.assertEqual(count, len(list_of_web_elements_employee_names), "Not all entries contain amb")

if __name__ == '__main__':
    unittest.main()