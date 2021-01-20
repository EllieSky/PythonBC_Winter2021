import unittest


def login(self, username, password):
    self.driver.find_element_by_id('txtUsername').send_keys(username) if username else None

    if password:
        self.driver.find_element_by_id('txtPassword').send_keys(password)

    self.driver.find_element_by_id('btnLogin').click()

if __name__ == '__main__':
    unittest.main()
