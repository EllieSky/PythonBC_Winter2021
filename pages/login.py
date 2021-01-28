from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, browser: Chrome):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def login(self, username='admin', password='password'):
        url = self.browser.current_url
        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        self.browser.find_element_by_id('btnLogin').click()

        self.wait.until(EC.url_changes(url)) if password and username else None
