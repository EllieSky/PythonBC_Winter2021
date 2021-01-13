import unittest
from selenium import webdriver
import time
from tests import CHROME_PATH




class OrangeHRMLogin(unittest.TestCase):

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver

    def tearDown(self) -> None:
        self.driver.quit()


    def test_orange_login(self):
        # Take browser out of SELF into local variable
        driver = self.driver
        driver.get("http://hrm-online.portnov.com/")
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




if __name__ == '__main__':
    unittest.main()
