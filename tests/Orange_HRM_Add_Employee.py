import unittest
from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select # works on the tags that have SELECT tag
from selenium.webdriver.support.wait import WebDriverWait
import pages
from fixtures.fixture import BaseFixture
from pages.login import LoginPage
import time

# Base fixture in Class imports the fixtures we created
class OrangeHRMEmpEmployeeSort(BaseFixture):

    def test_emp_emp_sorting(self):

        # Test Variables
        driver = self.driver
        desired_url = 'http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList?sortField=firstMiddleName&sortOrder=ASC'
        wait = WebDriverWait(driver, 15)
        expected_login_url = "http://hrm-online.portnov.com/symfony/web/index.php/auth/login"
        wait.until(EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_link_text("First (& Middle) Name").click()
        wait.until(EC.url_contains, "firstMiddleName&sortOrder=ASC")
        driver.find_element_by_id("empsearch_employee_name_empName").send_keys("this is a test")


        rows = len(driver.find_elements_by_xpath("//tbody/tr")) #count rows
        columns = len(driver.find_elements_by_xpath("//tbody/tr[1]/td")) # count th tags(columns)

        print(rows)
        print(columns)

        # for r in range(rows + 1):
        #     for c in range(columns + 1):
        #         names = driver.find_element_by_xpath("//tbody/tr/td[3]").text
        #         print(names)



        self.assertTrue(driver.current_url, expected_login_url)

        # Logging in with a newly created user

        self.login_page.login(user_name + employee_id, new_password)
        wait.until(EC.presence_of_element_located([By.ID, "welcome"]))
        welcome = driver.find_element_by_id("welcome").text
        self.assertEqual("Welcome Denis", welcome)





