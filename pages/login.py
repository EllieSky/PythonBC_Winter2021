class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username = 'admin', password = 'password'):

        self.browser.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            self.browser.find_element_by_id('txtPassword').send_keys(password)

        self.browser.find_element_by_id('btnLogin').click()

