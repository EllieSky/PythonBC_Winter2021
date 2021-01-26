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

    def test_emp_emp_sorting(self):

        driver = self.driver
        wait = WebDriverWait(driver, 15)


        wait.until(EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_link_text("First (& Middle) Name").click()
    # Waiting for sort to complete by checking URL change
        wait.until(EC.url_contains, "firstMiddleName&sortOrder=ASC")
        page_info = driver.find_element_by_xpath("//li[@class='desc']").text
        print(page_info)

        names_table = driver.find_elements_by_xpath("//tbody/tr/td[3]")
        list_of_names = []

    # Getting a list of First names from the page, adding them to the list and comparing with the same list but sorted.
        for i in range(len(names_table)):
            name = names_table[i].text.lower()
            list_of_names.append(name)
            print(list_of_names)
            self.assertEqual(list_of_names, sorted(list_of_names))







if __name__ == '__main__':
    unittest.main()
