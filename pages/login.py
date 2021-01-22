class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username="admin", password="password"):
        # enter username
        self.driver.find_element_by_id('txtUsername').send_keys(username) if username else None

        if password:
            # enter password
            self.driver.find_element_by_id('txtPassword').send_keys(password)

        # click Login button
        self.driver.find_element_by_id('btnLogin').click()