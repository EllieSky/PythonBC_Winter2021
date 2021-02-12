import os
import unittest

import requests

from tests import PROJ_PATH


class Yopmail(unittest.TestCase):
    def test_get_yopmail_en_page(self):

        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        # headers = {'User-Agent':'Mozilla/5.0 (iPod; CPU iPhone OS 12_0 like macOS) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/12.0 Mobile/14A5335d Safari/602.1.50'}
        url = 'http://www.yopmail.com/en/'

        response = requests.get(url, headers=headers)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.url.endswith('yopmail.com/en/'))
        self.assertIn('YOPmail - Disposable Email Address', response.text)

    def test_check_yopmail_inbox(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        url = 'http://www.yopmail.com/en/'

        content_type = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers.update(content_type)

        response2 = requests.post(url, headers=headers, data='yp=KAQRlBGH0BGN2ZmHkAmt2ZmL&login=tree')

        self.write_to_file(self._testMethodName + '2', response2.text)

        self.assertIn('YOPmail - Inbox', response2.text)

        # '&#64;' is the Alt Key Code for the '@' character
        # Unfortunately there is not easy decoding for it  :(
        self.assertIn('tree&#64;yopmail.com'.encode('utf-8'), response2.text)


    def test_foothill(self):
        resp1 = requests.get('http://books.foothill.edu/postList')
        token = resp1.cookies.get('__RequestVerificationToken')
        data = f'__RequestVerificationToken={token}&ClassifiedsName=Owl+Marketplace&AllowPostEditing=True&BookAuthor=BUTLERselectedCategory=0&submitButton=Search+Posts&selectedSort=0&CommentID=0&DeleteID=0&AbuseID=0&UpdateID=0&UpdatePrice=0&UpdateCategory=0'
        resp = requests.post('http://books.foothill.edu/postList',
                      headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data)
        self.write_to_file(self._testMethodName + '3', resp.text)


    def write_to_file(self, file_name, data):
        test_results_folder = f"{PROJ_PATH}/screenshots"
        if not os.path.exists(test_results_folder):
            os.mkdir(test_results_folder)

        with open(f"{test_results_folder}/{file_name}.html", 'w', encoding="utf-8") as file:
            file.write(data)

if __name__ == '__main__':
    unittest.main()
