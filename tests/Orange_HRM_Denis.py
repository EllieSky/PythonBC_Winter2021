import unittest
from selenium import webdriver
import time




class OrangeHRMLogin(unittest.TestCase):
    def test_orange_login(self):
        # username = "admin"
        # password = "password"
        driver = webdriver.Chrome()
        driver.maximize_window()
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
        driver.close()



if __name__ == '__main__':
    unittest.main()
