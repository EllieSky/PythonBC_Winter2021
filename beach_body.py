import time
import unittest
import os

from selenium import webdriver

from tests import CHROME_PATH


class BeachBody(unittest.TestCase):
    # Website is no longer active
    @unittest.skipUnless(os.environ.get('DEBUG'), 'Expected Failure')
    def test_get_started_button(self):
        browser = webdriver.Chrome(executable_path=CHROME_PATH)
        browser.get('https://www.beachbody.com/')

        browser.find_element_by_class_name('button').click()

        time.sleep(1)

        expected_url = 'https://www.beachbody.com/create-account?productCode=BODGEN&rc=BODGEN'
        actual_url = browser.current_url

        self.assertEqual(expected_url, actual_url)

        self.assertIn("create-account", actual_url)


if __name__ == '__main__':
    unittest.main()
