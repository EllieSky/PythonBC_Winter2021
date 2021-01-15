import time
import unittest

from selenium import webdriver


class BeachBody(unittest.TestCase):
    def test_get_started_button(self):
        browser = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        browser.get("https://www.beachbody.com/")
        browser.find_element_by_class_name("button").click()
        time.sleep(1)
        expected_url = "https://www.beachbody.com/create-account?productCode=BODGEN&rc=BODGEN"
        actual_url = browser.current_url
        self.assertEqual(expected_url, actual_url)
        self.assertIn("create-account", actual_url)


if __name__ == '__main__':
    unittest.main()
