import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select

from tests import CHROME_PATH


class EmpSearch(unittest.TestCase):

    def setUp(self) -> None:
        # browser session
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        browser.get("http://hrm-online.portnov.com/")
        # Take  local browser and store it into SELF
        self.browser = browser

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username, password):
        # enter username
        self.browser.find_element_by_id("txtUsername").send_keys(username) if username else None

        if password:
            # enter password
            self.browser.find_element_by_id("txtPassword").send_keys(password)

        # click Login button
        self.browser.find_element_by_id("btnLogin").click()

    def test_search_by_job_title(self):
        self.login("admin", "password")
        # self.browser.find_element_by_id("empsearch_job_title").send_keys("SDET")
        # OR
        # browser.find_element_by_id("empsearch_job_title").click()
        # self.browser.find_element_by_xpath('//*[@id="empsearch_job_title"]/option[9]').click

        # TODO: Add example of webdriver select
        # Example of webdriver select

        Select(self.browser.find_element_by_id("empsearch_job_title")).select_by_visible_text("SDET")
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@id='searchBtn']").click()

        result = self.browser.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]').text
        self.assertEqual('SDET', result)

        list_of_web_elements_jtitles = self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr/td[5]')

        for item in list_of_web_elements_jtitles:
            self.assertEqual('SDET', item.text)


if __name__ == '__main__':
    unittest.main()