import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.fixture import AdminLogin


class EmpSearch(AdminLogin):
    def test_first_middle_sort(self):

        self.wait.until(EC.presence_of_element_located([By.LINK_TEXT, 'First (& Middle) Name'])).click()
        self.wait.until(EC.url_contains('sortField=firstMiddleName&sortOrder=ASC'))


        # fn_list = []
        #
        # for el in list_of_fn_elements:
        #     fn_list.append(el.text.lower())
        #
        # self.assertListEqual(fn_list, sorted(fn_list))

        # try:
        #     pagination = self.browser.find_element_by_css_selector('.paging.top .desc').text.split()
        #     pagination[0].endswith(pagination[-1])
        # except NoSuchElementException:
        #     pass

        previous = ""
        while True:
            list_of_fn_elements = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[3]/a')
            for el in list_of_fn_elements:
                current = el.text.lower()
                self.assertGreaterEqual(current, previous)
                print(f"The current name '{current}' is after previous name '{previous}'")

                previous = current

            pagination = self.browser.find_elements_by_css_selector('.paging.top .desc')
            last_page = True
            if pagination:
                pages = pagination[0].text.split()
                last_page = pages[0].endswith(pages[-1])
            if last_page:
                break
            else:
                self.browser.find_element_by_css_selector('.next a').click()
                print("NEXT")



if __name__ == '__main__':
    unittest.main()
