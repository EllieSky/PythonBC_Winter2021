from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SystemUsersPage(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def add(self):
        self.browser.find_element_by_id('btnAdd').click()
        self.wait.until(EC.url_contains('/admin/saveSystemUser'))

    def wait_for_page_to_load(self):
        self.wait.until(EC.url_contains('/admin/viewSystemUsers'))
        self.wait.until(EC.presence_of_element_located((By.ID, 'systemUser-information')))

    def is_username_listed(self, username):
        result = self.browser.find_elements_by_link_text(username)
        return result if result else False   # returns the list of it's not EMPTY, else returns False
        # return True if result else False   # returns True if list is not EMPTY, otherwise returns False

    def get_user_id_for_username(self, username):
        try:
            user_web_element = self.browser.find_element_by_link_text(username)
            return user_web_element[0].get_attribute('href').split('=')[-1]
        except (NoSuchElementException, TypeError):
            raise ValueError(f'Could not determine user id, because username "{username}" is not listed on the page')

    def get_user_role_for_username(self, username):
        return self.browser.find_element_by_xpath(f"//a[text()='{username}']/ancestor::tr/td[3]").text

    def get_user_full_name_for_username(self, username):
        return self.browser.find_element_by_xpath(f"//a[text()='{username}']/following::td[1]").text