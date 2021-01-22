import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select # works on the tags that have SELECT tag

from pages.login import LoginPage


class OrangeHRMEmpSearch(unittest.TestCase):

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        driver.get("http://hrm-online.portnov.com/")
        self.login_page = LoginPage(driver)
        self.login_page.login()


    def tearDown(self) -> None:
        self.driver.quit()


    def test_emp_search_by_QAManager(self):
        driver = self.driver
        #self.login_page.login("admin", "password")            ### Login is called from a set up class, no need for this
        time.sleep(2)
        driver.find_element_by_css_selector("#empsearch_job_title > option:nth-child(8)").click()
        driver.find_element_by_id("searchBtn").click()
        time.sleep(2)
        # Select can be used as a selector for a dropdown
        #Select(driver.find_element_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(5)")).deselect_by_visible_text("QA Manager")
        job_title = driver.find_element_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(5)").text
        self.assertEqual("QA Manager", job_title)
        list_of_web_elamets_from_job_title = driver.find_elements_by_css_selector("#resultTable > tbody > tr:nth-child(1) > td:nth-child(5)")
        for item in list_of_web_elamets_from_job_title:
            self.assertEqual("QA Manager", item.text)








