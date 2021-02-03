import os
import unittest
import requests

from tests import PROJ_DIR


class Yopmail(unittest.TestCase):
    def test_get_yopmail_en_page(self):

        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
        url = "http://www.yopmail.com/en/"
        response = requests.get(url, headers=headers)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.url.endswith("mail.com/en/"))
        self.assertIn("YOPmail - Disposable Email Address", response.text)
        self.write_to_file(self._testMethodName, response.text)

    def test_check_yopmail_inbox(self):

        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
        url = "http://www.yopmail.com/en/"
        content_type = {"Content-Type" : "application/x-www-form-urlencoded"}
        headers.update(content_type)
        response2 = requests.post(url, headers=headers, data="yp: KAQNkZmt1ZmD1Zmt5AmLjZmD")
        self.write_to_file(self._testMethodName, response2.text)
        self.assertIn("YOPmail - Disposable Email Address", response2.text)




    def write_report_to_file(self, file, data):
        test_results_folder = f"{PROJ_DIR}/screenshots"  # Screenshot folder location
        if not os.path.exists(test_results_folder):  # If condition to create screenshot folde only if it does not exist
            os.mkdir(test_results_folder)
        test_name = self._testMethodName  # Assigning the test name to the screenshot below

        with open(f"{test_results_folder}/{file}.html", "w", encoding="utf-8") as file:
            file.write(data)


if __name__ == '__main__':
    unittest.main()
