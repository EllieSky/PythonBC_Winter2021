import unittest

from fixtures.fixture import AdminLogin
from menues.main_menu import MainMenu


class MainMenuTestSuite(AdminLogin):
    def test_localization_menu_item(self):
        menu = MainMenu(self.browser)
        menu.goto_admin_configuration_localization()
        self.assertTrue(self.browser.current_url.endswith('/admin/localization'))

    def test_admin_users_menu_item(self):
        menu = MainMenu(self.browser)
        menu.goto_admin_users()
        self.assertTrue(self.browser.current_url.endswith('/admin/viewSystemUsers'))


if __name__ == '__main__':
    unittest.main()
