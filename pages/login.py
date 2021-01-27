from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def login(self, username="admin", password="password"):
        # enter username
        url = self.driver.current_url
        self.driver.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            # enter password
            self.driver.find_element_by_id('txtPassword').send_keys(password)

        # click Login button
        self.driver.find_element_by_id('btnLogin').click()

        self.wait.until(EC.url_changes(url)) if username and password else None