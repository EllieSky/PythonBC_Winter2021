import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from api.api import Api
from fixtures.fixture import AdminLogin


class AdminPageCreateUser(AdminLogin):
    def test_create_ess_user(self):
        self.browser.find_element_by_id('menu_admin_viewAdminModule').click()
        self.wait.until(EC.url_contains('/admin/viewSystemUsers'))
        self.wait.until(EC.presence_of_element_located((By.ID, 'systemUser-information')))

        self.browser.find_element_by_id('btnAdd').click()
        self.wait.until(EC.url_contains('/admin/saveSystemUser'))
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        #                                                 '#systemUser_employeeName_empName.inputFormatHint')))
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'systemUser_employeeName_empName'))).send_keys('Charles Marsh')
        self.browser.find_element_by_id('systemUser_userName').send_keys('CharlesMarsh')
        self.browser.find_element_by_id('systemUser_password').send_keys('password')
        self.browser.find_element_by_id('systemUser_confirmPassword').send_keys('password')
        self.browser.find_element_by_id('btnSave').click()

        self.wait.until(EC.url_contains('/admin/viewSystemUsers'))
        self.wait.until(EC.presence_of_element_located((By.ID, 'systemUser-information')))

        user_created = self.browser.find_elements_by_link_text('CharlesMarsh')
        self.assertTrue(user_created)

        self.user_id = user_created[0].get_attribute('href').split('=')[-1]

        self.assertEqual('ESS', self.browser.find_element_by_xpath("//a[text()='caleb']/ancestor::tr/td[3]").text)
        # Same WebElement as above
        self.assertEqual('ESS', self.browser.find_element_by_xpath("//a[text()='caleb']/following::td[1]").text)
        self.assertTrue(self.browser.find_elements_by_xpath('//td[text()="Charles Marsh"]'))

    def tearDown(self) -> None:
        if hasattr(self, 'user_id'):
            api = Api()
            api.sign_in()
            api.delete_user(self.user_id)
        super().tearDown()



if __name__ == '__main__':
    unittest.main()
