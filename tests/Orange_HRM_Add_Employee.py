import unittest
from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select # works on the tags that have SELECT tag
from selenium.webdriver.support.wait import WebDriverWait
import pages
import time
from fixtures.fixture import BaseFixture
from pages.login import LoginPage

# Base fixture in Class imports the fixtures we created
class OrangeHRMEmpAddEmployee(BaseFixture):

    def test_emp_add_user(self):
        #self.login_page.login('admin', 'password') Dont need this as the function is called from a set up class.

        # Test Variables
        driver = self.driver
        desired_url = 'http://hrm-online.portnov.com/symfony/web/index.php/pim/addEmployee'
        wait = WebDriverWait(driver, 15)
        first_name = "Denis"
        last_name = "Frolov"
        user_name = (first_name + last_name).lower()
        new_password = "password"
        picture = "C:/Users/Denis/Dropbox/My PC (DESKTOP-KJ79GMA)/Documents/Silver Auto Python Bootcamp/upload files/test.jpg"
        expected_login_url = "http://hrm-online.portnov.com/symfony/web/index.php/auth/login"

        # Wait provided by Ellie

        wait.until(
            EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_id("btnAdd").click()

        # Two more Waits for practice

        wait.until(EC.url_to_be(desired_url))
        wait.until(EC.presence_of_element_located([By.ID, "firstName"]))
        driver.find_element_by_id("firstName").send_keys(first_name)
        driver.find_element_by_id("lastName").send_keys(last_name)
        employee_id = driver.find_element_by_id("employeeId").get_attribute("value")

        # Uploading a test profile picture

        upload_file = driver.find_element_by_id("photofile")
        upload_file.send_keys(picture)
        driver.find_element_by_id("chkLogin").click()

        # Waiting for the fields to become visible

        wait.until(EC.visibility_of_element_located([By.ID, "user_name"]))
        driver.find_element_by_id("user_name").send_keys(user_name + employee_id)
        driver.find_element_by_id("user_password").send_keys(new_password)
        driver.find_element_by_id("re_password").send_keys(new_password)
        driver.find_element_by_id("status").click()
        driver.find_element_by_id("btnSave").click()


        # Making sure Personal Details is displayed

        wait.until((EC.presence_of_element_located([By.XPATH, "//h1[contains(text(),'Personal Details')]"])))
        driver.find_element_by_id("welcome").click()

        # This is a wait for the logout overlay to be visible

        wait.until(EC.visibility_of_element_located([By.XPATH, "//a[contains(text(),'Logout')]"]))
        driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        self.assertTrue(driver.current_url, expected_login_url)

        # Logging in with a newly created user

        self.login_page.login(user_name + employee_id, new_password)
        wait.until(EC.presence_of_element_located([By.ID, "welcome"]))
        welcome = driver.find_element_by_id("welcome").text
        self.assertEqual("Welcome Denis", welcome)




