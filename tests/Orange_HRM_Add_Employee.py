import unittest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select # works on the tags that have SELECT tag
from selenium.webdriver.support.wait import WebDriverWait


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
        desired_url = 'http://hrm-online.portnov.com/symfony/web/index.php/pim/addEmployee'
        wait = WebDriverWait(driver, 15)
        self.login('admin', 'password')
        wait.until(EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))
        driver.find_element_by_id("btnAdd").click()
        # TODO Need to figure out why the following Waits are not working: #wait.until(EC.url_contains('/viewEmployeeList'))
        #  #wait.until(EC.element_to_be_clickable([By.ID, "btnAdd"]))
        wait.until(EC.url_to_be(desired_url))
        wait.until(EC.presence_of_element_located([By.ID, "middleName"]))
        driver.find_element_by_id("firstName").send_keys("Denis")
        driver.find_element_by_id("lastName").send_keys("Frolov")
        employee_id = driver.find_element_by_id("employeeId").get_attribute("value")
        print(employee_id)
        upload_file = driver.find_element_by_id("photofile")
        upload_file.send_keys("C:/Users/Denis/Dropbox/My PC (DESKTOP-KJ79GMA)/Documents/Silver Auto Python Bootcamp/upload files/test.jpg")
        driver.find_element_by_id("chkLogin").click()
        wait.until(EC.visibility_of_element_located([By.ID, "user_name"]))
        driver.find_element_by_id("user_name").send_keys("Denisfrolov" + employee_id)
        driver.find_element_by_id("user_password").send_keys("password")
        driver.find_element_by_id("re_password").send_keys("password")
        driver.find_element_by_id("status").click()
        driver.find_element_by_id("btnSave").click()
        wait.until(EC.url_changes)
        wait.until((EC.presence_of_element_located([By.ID, "btnSave"])))
        driver.find_element_by_id("welcome").click()
        wait.until(EC.visibility_of_element_located([By.XPATH, "//a[contains(text(),'Logout')]"]))
        driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        self.assertTrue(driver.current_url, "http://hrm-online.portnov.com/symfony/web/index.php/auth/login")

# Logging in with a newly created user

        self.login('Denisfrolov' + employee_id, 'password')
        wait.until(EC.presence_of_element_located([By.ID, "welcome"]))
        welcome = driver.find_element_by_id("welcome").text
        self.assertEqual("Welcome Denis", welcome)





