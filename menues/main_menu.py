from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.system_users import SystemUsersPage


class MainMenu(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def goto_admin_tab(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'menu_admin_viewAdminModule'))).click()
        SystemUsersPage(self.browser).wait_for_page_to_load()
