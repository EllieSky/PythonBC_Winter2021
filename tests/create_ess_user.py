import time
import unittest

from api.api import Api
from fixtures.fixture import AdminLogin
from menues.main_menu import MainMenu
from pages.add_system_user import AddSystemUserPage
from pages.system_users import SystemUsersPage


class AdminPageCreateUser(AdminLogin):
    def test_create_ess_user(self):
        sys_users = SystemUsersPage(self.browser)
        add_sys_user = AddSystemUserPage(self.browser)
        main_menu = MainMenu(self.browser)

        name = "Anita Jones"
        username = "AnitaJones" + str(time.time())[-6::]

        main_menu.goto_admin_tab()
        # self.browser.find_element_by_id('menu_admin_viewAdminModule').click()
        # self.wait.until(EC.url_contains('/admin/viewSystemUsers'))
        # self.wait.until(EC.presence_of_element_located((By.ID, 'systemUser-information')))

        sys_users.add()
        # self.browser.find_element_by_id('btnAdd').click()
        # self.wait.until(EC.url_contains('/admin/saveSystemUser'))
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        #                                                 '#systemUser_employeeName_empName.inputFormatHint')))

        add_sys_user.fill_out_user_form(name, username, 'password', 'password')
        # self.wait.until(EC.presence_of_element_located(
        #     (By.ID, 'systemUser_employeeName_empName'))).send_keys('Charles Marsh')
        # self.browser.find_element_by_id('systemUser_userName').send_keys('CharlesMarsh')
        # self.browser.find_element_by_id('systemUser_password').send_keys('password')
        # self.browser.find_element_by_id('systemUser_confirmPassword').send_keys('password')
        add_sys_user.save()
        # self.browser.find_element_by_id('btnSave').click()

        sys_users.wait_for_page_to_load()
        # self.wait.until(EC.url_contains('/admin/viewSystemUsers'))
        # self.wait.until(EC.presence_of_element_located((By.ID, 'systemUser-information')))

        user_created = sys_users.is_username_listed(username)
        # user_created = self.browser.find_elements_by_link_text('CharlesMarsh')
        self.assertTrue(user_created)

        self.user_id = sys_users.get_user_id_for_username(username)
        # self.user_id = user_created[0].get_attribute('href').split('=')[-1]

        role = sys_users.get_user_role_for_username(username)
        self.assertEqual('ESS', role)

        user_full_name = sys_users.get_user_full_name_for_username(username)
        self.assertEqual(name, user_full_name)
        # self.assertEqual('ESS', self.browser.find_element_by_xpath("//a[text()='caleb']/ancestor::tr/td[3]").text)
        # Same WebElement as above
        # self.assertEqual('ESS', self.browser.find_element_by_xpath("//a[text()='caleb']/following::td[1]").text)
        # self.assertTrue(self.browser.find_elements_by_xpath('//td[text()="Charles Marsh"]'))

    def tearDown(self) -> None:
        if hasattr(self, 'user_id'):
            api = Api()
            api.sign_in()
            api.delete_user(self.user_id)
        super().tearDown()



if __name__ == '__main__':
    unittest.main()
