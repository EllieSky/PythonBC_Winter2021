from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from pages.system_users import SystemUsersPage


class MainMenu(Base):
    admin = (By.ID, 'menu_admin_viewAdminModule')
    user_management = (By.ID, 'menu_admin_UserManagement')
    admin_configure = (By.ID, 'menu_admin_Configuration')
    localization = (By.ID, 'menu_admin_localization')
    admin_users = (By.ID, 'menu_admin_viewSystemUsers')

    def goto_admin_tab(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'menu_admin_viewAdminModule'))).click()
        SystemUsersPage(self.browser).wait_for_page_to_load()


    def goto_admin_configuration_localization(self):
        # self.browser.find_element(By.ID, 'menu_admin_viewAdminModule')
        # same as above
        admin_el = self.browser.find_element(*self.admin)
        user_man_el = self.browser.find_element(*self.user_management)
        conf_el = self.browser.find_element(*self.admin_configure)
        local_el = self.browser.find_element(*self.localization)


        action = ActionChains(self.browser)
        action.move_to_element(admin_el)
        action.pause(0.5)
        action.move_to_element(user_man_el)
        action.pause(1)
        action.move_to_element(conf_el)
        action.pause(0.25)
        action.click(local_el)

        # action.move_to_element(self.wait_for_el(self.admin))
        # action.move_to_element(self.wait_for_el(self.user_management))
        # action.move_to_element(self.wait_for_el(self.configure))
        # action.click(self.wait_for_el(self.localization))

        action.perform()

    def goto_admin_users(self):
        action = ActionChains(self.browser)
        action\
            .move_to_element(self.browser.find_element(*self.admin))\
            .pause(.33)\
            .move_to_element(self.browser.find_element(*self.user_management))\
            .click(self.browser.find_element(*self.admin_users)).perform()

    def wait_for_el(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
