from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from pages.login import LoginPage


class UserMenu(Base):
    def logout(self):
        self.browser.find_element_by_id("welcome").click()

        self.wait.until(EC.visibility_of_element_located(
            [By.LINK_TEXT, "Logout"]
        )).click()

        LoginPage(self.browser).wait_for_page_to_load()

    def get_welcome_message(self):
        return self.wait.until(EC.presence_of_element_located(
            [By.ID, 'welcome']
        )).text
