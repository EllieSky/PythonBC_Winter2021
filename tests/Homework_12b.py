import os
import unittest
import requests

from tests import CHROME_PATH, PROJ_PATH


class Foothill(unittest.TestCase):

    def test_get_foothill_en_page(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        url = 'http://books.foothill.edu/postList'

        response = requests.get(url, headers=headers)

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.url.endswith('foothill.edu/postList'))
        self.assertIn('__RequestVerificationToken', response.text)

        self.write_to_file(self._testMethodName, response.text)

    def test_search_book_foothill(self):
        url = 'http://books.foothill.edu/postList'
        response = requests.get(url)
        token = response.cookies.get('__RequestVerificationToken')

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = f'__RequestVerificationToken={token}&ClassifiedsName=Owl+Marketplace&AllowPostEditing=True&BookAuthor=moore&selectedCategory=0&submitButton=Search+Posts&selectedSort=0&CommentID=0'

        # response2 = requests.post(url, headers=headers, data=data)
        response2 = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data)

        self.assertIn('978140120841', response2.text)

        self.write_to_file(self._testMethodName + '2', response2.text)








    def write_to_file(self, file_name, data):
        test_results_folder = f"{PROJ_PATH}/screenshots"
        if not os.path.exists(test_results_folder):
            os.mkdir(test_results_folder)

        with open(f"{test_results_folder}/{file_name}.html", 'w', encoding="utf-8") as file:
            file.write(data)


if __name__ == '__main__':
    unittest.main()
