import os
import unittest
import requests

from tests import CHROME_PATH, PROJ_PATH


class Yopmail(unittest.TestCase):
    def test_get_yopmail_en_page(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        # below is example of User-Agent for mobile device: iPhone 12
        # headers = {'User-Agent':'Mozilla/5.0 (iPod; CPU iPhone OS 12_0 like macOS) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/12.0 Mobile/14A5335d Safari/602.1.50'}
        url = 'http://www.yopmail.com/en/'

        # response = requests.get(url='http://www.yopmail.com/en/', headers=headers)
        response = requests.get(url, headers=headers)
        # OR you can use:
        # response = requests.get('http://www.yopmail.com/en/', headers=headers)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.url.endswith('yopmail.com/en/'))
        self.assertIn('YOPmail - Disposable Email Address', response.text)

        # test_results_folder = f"{PROJ_PATH}/screenshots"
        # if not os.path.exists(test_results_folder):
        #     os.mkdir(test_results_folder)
        # test_name = self._testMethodName
        #
        # with open(f"{test_results_folder}/{test_name}.html", 'w', encoding="utf-8") as file:
        #     file.write(response.text)
        # We rewriting code above to make saving to file as function:

        self.write_to_file(self._testMethodName, response.text)

    def test_check_yopmail_inbox(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

        url = 'http://www.yopmail.com/en/'

        content_type = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers.update(content_type)

        response2 = requests.post(url, headers=headers, data='yp: MAQtmZwL1ZwxlAQp2ZQZ1BQV&login=tree')
        self.write_to_file(self._testMethodName + '2', response2.text)
        # self.assertIn('tree@yopmail.com'.encode('utf-8'), response2.text)
        self.assertIn('YOPmail - Inbox', response2.text)

        # Below GET request is not working, need more debugging:
        # response3 = requests.get(url + 'inbox.php', headers=headers,
        #                          data='login=tree&p=1&spam=true&yf=005&yp=WBGDmZmxjBGH1ZwZ2AmH1At&yj=TZmZmZmNkAmx1AwNkZwDkZGN&v=3.1')
        # self.write_to_file(self._testMethodName + '3', response3.text)

    def write_to_file(self, file_name, data):
        test_results_folder = f"{PROJ_PATH}/screenshots"
        if not os.path.exists(test_results_folder):
            os.mkdir(test_results_folder)

        with open(f"{test_results_folder}/{file_name}.html", 'w', encoding="utf-8") as file:
            file.write(data)

        pass


if __name__ == '__main__':
    unittest.main()
