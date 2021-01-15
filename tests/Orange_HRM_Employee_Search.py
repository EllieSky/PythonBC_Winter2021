import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select # works on the tags that have SELECT tag


class OrangeHRMEmpSearch(unittest.TestCase):

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        driver.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def login(self, username, password):
        # enter username
        self.driver.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            # enter password
            self.driver.find_element_by_id('txtPassword').send_keys(password)

        # click Login button
        self.driver.find_element_by_id('btnLogin').click()


    def test_emp_search_by_QAManager(self):
        driver = self.driver
        self.login("admin", "password")
        time.sleep(2)
        driver.find_element_by_css_selector("#empsearch_job_title > option:nth-child(8)").click()
        driver.find_element_by_id("searchBtn").click()
        time.sleep(2)
        # Select can be used as a selector for a dropdown
        #Select(driver.find_element_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(5)")).deselect_by_visible_text("QA Manager")
        job_title = driver.find_element_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(5)").text
        self.assertEqual("QA Manager", job_title)
        list_of_webelamets_from_job_title = driver.find_elements_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(5)")
        for item in list_of_webelamets_from_job_title:
            self.assertEqual("QA Manager", item.text)








