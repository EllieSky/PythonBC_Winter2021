import unittest
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from fixtures.fixture import BaseFixture


class JS_Demo(BaseFixture):
    def test_google_search_result_new_window(self):
        self.browser.get('https://www.google.com/search')
        self.browser.find_element(By.NAME, 'q').send_keys('dogs', Keys.ENTER)

        search_results = self.browser.find_elements(By.CSS_SELECTOR, 'a h3')
        random_search_result = random.choice(search_results)
        page_title_of_random_search_result = random_search_result.text

        # sometimes webdriver element.text doesn't work and return empty str
        # the work around is to use JS when it doesn't work via webdriver
        if not page_title_of_random_search_result:
            page_title_of_random_search_result = self.browser.execute_script('return arguments[0].textContent', random_search_result)

        href = random_search_result.find_element(By.XPATH, './/..').get_attribute('href')
        # js_template = f"window.open('{href}')"
        # self.browser.execute_script(js_template)
        # OR using *args
        js_template = "window.open(arguments[0])"
        num_windows_before = len(self.browser.window_handles)
        self.browser.execute_script(js_template, href)

        self.wait.until(EC.number_of_windows_to_be(num_windows_before + 1))
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[-1])

        self.assertIn(self.browser.title, page_title_of_random_search_result)


if __name__ == '__main__':
    unittest.main()
