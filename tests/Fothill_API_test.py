import os
import unittest
import requests

from tests import PROJ_DIR


class Foothill(unittest.TestCase):
    def test_foothill__page(self):

        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
        url = "http://books.foothill.edu/postList"
        response = requests.get(url, headers=headers)
        cookie = response.cookies.get('__RequestVerificationToken')
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.url.endswith("edu/postList"))
        self.assertIn("Foothill College Campus Store", response.text)
        self.write_report_to_file(self._testMethodName, response.text)



    def test_check_foothill_results(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        url = 'http://books.foothill.edu/postList'
        response2 = requests.get(url, headers=headers)
        content_type = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers.update(content_type)
        cookie = response2.cookies.get('__RequestVerificationToken')
        response2 = requests.post(url, headers=headers, cookies=cookie, data="BookAuthor: Moore",)
        self.write_report_to_file(self._testMethodName + '2', response2.text)
        self.assertTrue(response2.url.endswith("edu/postList"))

    def write_report_to_file(self, file, data):
        test_results_folder = f"{PROJ_DIR}/screenshots"  # Screenshot folder location
        if not os.path.exists(test_results_folder):  # If condition to create screenshot folder only if it does not exist
            os.mkdir(test_results_folder)
        test_name = self._testMethodName  # Assigning the test name to the screenshot below

        with open(f"{test_results_folder}/{file}.html", "w", encoding="utf-8") as file:
            file.write(data)


if __name__ == '__main__':
    unittest.main()
