mport unittest
from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select # works on the tags that have SELECT tag
from selenium.webdriver.support.wait import WebDriverWait
import pages
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

        wait.until(EC.presence_of_element_located([By.CSS_SELECTOR, '#empsearch_employee_name_empName.inputFormatHint']))