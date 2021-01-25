import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from fixtures.fixture import BaseFixture
from pages.login import LoginPage
from tests import CHROME_PATH


class EmployeeSort(BaseFixture):

    def test_sort_employee_list(self):
        wait = WebDriverWait(self.browser, 5)
        self.login_page.login()
        wait.until(EC.url_contains("/pim/viewEmployeeList"))
        wait.until(EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        wait.until(EC.presence_of_element_located([By.LINK_TEXT, "First (& Middle) Name"]))
        self.browser.find_element_by_link_text("First (& Middle) Name").click()
        wait.until(EC.url_contains('/pim/viewEmployeeList?sortField=firstMiddleName&sortOrder=ASC'))

        # get info about qty of names in the list: 1-50 of 74
        page_info = self.browser.find_element_by_xpath("//li[@class='desc']").text
        # break info into list '1-50' 'of' '74'
        page_info = page_info.split()
        # get total names count
        names_qty = int(page_info[2])
        # split first entry 1-50 into list by "-" sign and get last name - i.e. qty of names per page
        names_per_page = int(page_info[0].split("-")[1])
        # calculate number of pages and round it to nearest int
        pages_count = int(names_qty / names_per_page + 0.999)

        for page_index in range(pages_count):

            list_of_web_elements_employee_names = self.browser.find_elements_by_xpath("//tbody/tr/td[3]")
            names_list =[]
            temp_list = []

            for i in range(len(list_of_web_elements_employee_names)):
                name = list_of_web_elements_employee_names[i].text.lower()
                names_list.append(name)
                temp_list.append(name)

            print("names_list: " + str(names_list))
            print("temp_list: " + str(temp_list))

            temp_list.sort()
            print("Sorted temp_list: " + str(temp_list))

            self.assertEqual(temp_list, names_list, "Names are sorted incorrectly")

            if page_index != pages_count - 1:
                self.browser.find_element_by_link_text("Next").click()
                wait.until(EC.url_contains('/pim/viewEmployeeList'))


if __name__ == '__main__':
    unittest.main()
