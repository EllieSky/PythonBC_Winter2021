from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage


class SystemUsersPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = '/admin/viewSystemUsers'
        self.page_header = 'System Users'

    def add(self):
        self.browser.find_element_by_id('btnAdd').click()
        self.wait.until(EC.url_contains('/admin/saveSystemUser'))

    def is_username_listed(self, username):
        result = self.browser.find_elements_by_link_text(username)
        # return result if result else False      # returns the list of it's not EMPTY, else returns False
        return True if result else False      # returns True if list is not EMPTY, otherwise returns False

    def get_user_id_for_username(self, username):
        try:
            user_web_element = self.browser.find_element_by_link_text(username)
            return user_web_element.get_attribute('href').split('=')[-1]
        except NoSuchElementException:
            raise ValueError(f'Could not determine user id, because username "{username}" is not listed on the page')

    def get_user_role_for_username(self, username):
        return self.browser.find_element_by_xpath(f"//a[text()='{username}']/ancestor::tr/td[3]").text

    def get_user_full_name_for_username(self, username):
        return self.browser.find_element_by_xpath(f"//a[text()='{username}']/following::td[2]").text