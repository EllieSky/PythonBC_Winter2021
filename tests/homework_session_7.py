import unittest
from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from tests import CHROME_PATH


class OrangeHRMUserSearch(unittest.TestCase):

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        driver.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            self.driver.find_element_by_id('txtPassword').send_keys(password)

        self.driver.find_element_by_id('btnLogin').click()

    def test_user_by_emp_id(self):
        driver = self.driver
        self.login("admin", "password")
        time.sleep(1)
        driver.find_element_by_id("empsearch_id").send_keys("319659")
        driver.find_element_by_id("searchBtn").click()
        result = driver.find_elements_by_xpath("//table/tbody/tr")
        for item in result:
            self.assertIn("319659", item.text)
        id = driver.find_element_by_xpath("//a[contains(text(),'319659')]").text
        self.assertEqual("319659", id)
        list_of_items = driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')
        quantity = len(list_of_items)
        self.assertEqual(1, quantity)



    def test_user_by_name(self):
        driver = self.driver
        self.login("admin", "password")
        time.sleep(1)
        driver.find_element_by_id("empsearch_employee_name_empName").send_keys("David")
        # driver.find_element_by_id("empsearch_employee_name_empName").send_keys("David", Keys.ESCAPE) # This does not work on Chrome
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_id("searchBtn").click()
        result = driver.find_elements_by_xpath("//table/tbody/tr")
        for item in result:
            self.assertIn("David", item.text)
        quantity = len(result)
        self.assertEqual(2, quantity)



    def test_user_by_name_2B(self):
        driver = self.driver
        self.login("admin", "password")
        time.sleep(1)
        name = driver.find_element_by_id("empsearch_employee_name_empName").send_keys("amb")
        # driver.find_element_by_id("empsearch_employee_name_empName").send_keys("David", Keys.ESCAPE) # This does not work on Chrome
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_id("searchBtn").click()
        first_name = driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr/td[3]/a")
        last_name = driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr/td[4]/a")
        for i in last_name:
            for y in first_name:
                if name in (i.text, y.text):
                    self.assertIn("amb", i.text, y.text)




if __name__ == '__main__':
    unittest.main()
