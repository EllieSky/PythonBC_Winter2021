import unittest

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

    def test_emp_sorting_page_one(self): # This is a first part for page one amd next page click

        driver = self.driver
        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_link_text("First (& Middle) Name").click()
    # Waiting for sort to complete by checking URL change
        wait.until(EC.url_contains, "firstMiddleName&sortOrder=ASC")
    # Introducing Variables
        names_table = driver.find_elements_by_xpath("//tbody/tr/td[3]")
        list_of_names = []
        next_button = driver.find_element_by_xpath("//*/div[1]/ul/li[6]/a")
    # Getting a list of First names from the page, adding them to the list and comparing with the same list but sorted.

        for i in range(len(names_table)):
            name = names_table[i].text.lower()
            list_of_names.append(name)
            self.assertEqual(list_of_names, sorted(list_of_names))

    # Clicking next button if there is more than one page

        if next_button.is_displayed():
            next_button.click()
            wait.until(EC.url_contains, "viewEmployeeList")
            driver.quit()
        else:
            print("There is only one page")

    def test_emp_sorting_with_next_page_validation(self): # This is a second part of HW with validation of page 2

        driver = self.driver
        wait = WebDriverWait(driver, 15)

        wait.until(
            EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_link_text("First (& Middle) Name").click()
        # Waiting for sort to complete by checking URL change
        wait.until(EC.url_contains, "firstMiddleName&sortOrder=ASC")
        next_button = driver.find_element_by_xpath("//*/div[1]/ul/li[6]/a")
        names_table = driver.find_elements_by_xpath("//tbody/tr/td[3]")
        list_of_names = []

        while True:
            try:
                names_table = driver.find_elements_by_xpath("//tbody/tr/td[3]")

                for i in range(len(names_table)):
                    name = names_table[i].text.lower()
                    list_of_names.append(name)
                    print(list_of_names)
                    self.assertEqual(list_of_names, sorted(list_of_names))

                wait.until(EC.url_contains, "viewEmployeeList")
                driver.find_element_by_xpath("//*/div[1]/ul/li[6]/a").click()
            except:
                break


        driver.quit()

if __name__ == '__main__':
    unittest.main()
