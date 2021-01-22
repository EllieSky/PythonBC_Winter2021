import unittest
from selenium import webdriver
import time

from pages.login import LoginPage
from tests import CHROME_PATH




class OrangeHRMLogin(unittest.TestCase):

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        driver.get("http://hrm-online.portnov.com/")



    def tearDown(self) -> None:
        self.driver.quit()


    def login(self, username, password):
        # enter username
        self.driver.find_element_by_id('txtUsername').send_keys(username)
        # enter password
        self.driver.find_element_by_id('txtPassword').send_keys(password)
        # click Login button
        self.driver.find_element_by_id('btnLogin').click()

    def test_orange_login(self):
        # Take browser out of SELF into local variable
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_name("Submit").click()
        time.sleep(2)
        assert driver.title == "OrangeHRM"
        welcome_admin = driver.find_element_by_id("welcome").text
        #assert welcome_admin.is_displayed()
        expected_url = "http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList"
        self.assertEqual(expected_url, "http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList")
        self.assertTrue(driver.current_url.endswith("pim/viewEmployeeList"))
        self.assertEqual("Welcome Admin", welcome_admin)


    def test_negative_scenario_one(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_name("Submit").click()
        error_one = driver.find_element_by_id("spanMessage")
        assert error_one.is_displayed()
        error_one = driver.find_element_by_id("spanMessage").text
        self.assertEqual("Username cannot be empty", error_one)

    def test_negative_scenario_two(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_name("Submit").click()
        error_two = driver.find_element_by_id("spanMessage")
        assert error_two.is_displayed()
        error_two = driver.find_element_by_id("spanMessage").text
        self.assertEqual("Password cannot be empty", error_two)

    def test_negative_scenario_three(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_name("Submit").click()
        error_three = driver.find_element_by_id("spanMessage")
        assert error_three.is_displayed()
        error_three = driver.find_element_by_id("spanMessage").text
        self.assertEqual("Username cannot be empty", error_three)

    def test_negative_scenario_four(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("txtUsername").send_keys("admin1")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_name("Submit").click()
        error_four = driver.find_element_by_id("spanMessage")
        assert error_four.is_displayed()
        error_four = driver.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_four)
        self.assertTrue(driver.current_url.endswith("validateCredentials"))

    def test_negative_scenario_five(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("txtUsername").send_keys("ADMIN")
        driver.find_element_by_id("txtPassword").send_keys("PASSWORD")
        driver.find_element_by_name("Submit").click()
        error_five = driver.find_element_by_id("spanMessage")
        assert error_five.is_displayed()
        error_four = driver.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_four)
        self.assertTrue(driver.current_url.endswith("validateCredentials"))

    def test_negative_scenario_six(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("txtUsername").send_keys("&^*%$#%")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_name("Submit").click()
        error_six = driver.find_element_by_id("spanMessage")
        assert error_six.is_displayed()
        error_four = driver.find_element_by_id("spanMessage").text
        self.assertEqual("Invalid credentials", error_four)
        self.assertTrue(driver.current_url.endswith("validateCredentials"))

if __name__ == '__main__':
    unittest.main()
