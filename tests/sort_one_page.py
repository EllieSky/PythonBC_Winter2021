import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import AdminLogin


class SortByName(AdminLogin):
    def test_sort(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.url_contains('/pim/viewEmployeeList'))

        wait.until(EC.presence_of_element_located(
            [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))

        self.browser.find_element_by_link_text('First (& Middle) Name').click()

        wait.until(EC.presence_of_element_located(
            [By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))

        list_of_names = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]')

        list_of_names1 = []

        for i in range(len(list_of_names)):
            name = list_of_names[i].text
            print(name)
            list_of_names1.append(name)

        print(list_of_names1)

        list_of_names2 = list_of_names1.copy()
        list_of_names3 = sorted(list_of_names2)

        print(list_of_names3)

        for i in range(len(list_of_names3)):
            self.assertListEqual(list_of_names1, list_of_names3)

if __name__ == '__main__':
    unittest.main()
