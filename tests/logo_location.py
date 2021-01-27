import unittest

from fixtures.fixture import BaseFixture


class LogoLocation(BaseFixture):

    def test_logo_top_left(self):
        self.driver.maximize_window()

        # determine size for the document
        body = self.driver.find_element_by_tag_name('body').size

        # determine top left quadrant
        # skipped - see below

        logo = self.driver.find_element_by_css_selector('#branding img')
        # get logo location
        logo_location = logo.location

        # get logo size
        logo_size = logo.size

        # get logo bottom right bound
        logo_bottom = logo_location['y'] + logo_size['height']
        logo_right = logo_location['x'] + logo_size['width']

        # assert
        self.assertLess(logo_bottom, body['height']/2)
        self.assertLess(logo_right, body['width']/200)


if __name__ == '__main__':
    unittest.main()