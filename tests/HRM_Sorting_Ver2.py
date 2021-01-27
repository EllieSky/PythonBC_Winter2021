import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select  # works on the tags that have SELECT tag
from selenium.webdriver.support.wait import WebDriverWait
import pages
from fixtures.fixture import BaseFixture
from pages.login import LoginPage
import time


# Base fixture in Class imports the fixtures we created
class OrangeHRMEmpEmployeeSort(BaseFixture):

    def test_emp_search_by_sorting(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_link_text("First (& Middle) Name").click()
        # Waiting for sort to complete by checking URL change
        wait.until(EC.url_contains, "firstMiddleName&sortOrder=ASC")
        names_table = driver.find_elements_by_xpath("//tbody/tr/td[3]")

        # list_of_names = []
        #
        # for i in names_table:
        #     list_of_names.append(i.text.lower())
        #
        # self.assertEqual(list_of_names, sorted(list_of_names))

        previous = ""

        for el in names_table:
            current = el.text.lower()
            self.assertGreaterEqual(current, previous)

            previous = current





if __name__ == '__main__':
    unittest.main()
