import os
import unittest
import requests

from tests import CHROME_PATH, PROJ_PATH


class Foothill(unittest.TestCase):

    def test_get_foothill_postList_page(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

        url = 'http://books.foothill.edu/postList'

        response = requests.get(url, headers=headers)

        html = response.text

        html_keyword = '<input name="__RequestVerificationToken"'

        position = html.find(html_keyword)

        token2 = html[position:].split('\n')[0].split(' ')[3].split('=')[1]

        # remove ""
        token2 = token2[1:len(token2)-1]

        print(token2)

        os.environ['__RequestVerificationToken'] = response.cookies.get('__RequestVerificationToken')

        os.environ['__RequestVerificationToken2'] = token2

        print(os.environ['__RequestVerificationToken'])
        print(os.environ['__RequestVerificationToken2'])

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.url.endswith('foothill.edu/postList'))
        self.assertIn('__RequestVerificationToken', response.text)

        self.write_to_file(self._testMethodName, response.text)

    def test_search_by_author_books_foothill(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36' }

        url = 'http://books.foothill.edu/postList'

        content_type = {'Content-Type': 'application/x-www-form-urlencoded'}

        headers.update(content_type)

        cookies = {'__RequestVerificationToken': os.environ['__RequestVerificationToken']}

        data = {'__RequestVerificationToken': os.environ['__RequestVerificationToken2'], 'ClassifiedsName': 'Owl Marketplace', 'AllowPostEditing': 'True', 'BookAuthor': 'moore', 'submitButton': 'Search Posts'}

        response2 = requests.post(url, headers=headers, data=data, cookies=cookies)

        self.write_to_file(self._testMethodName + '2', response2.text)

        self.assertIn('Your Owl Marketplace allows you to view and post textbooks for sale', response2.text)

        self.assertIn('978140120841', response2.text)



    def write_to_file(self, file_name, data):
        test_results_folder = f"{PROJ_PATH}/screenshots"
        if not os.path.exists(test_results_folder):
            os.mkdir(test_results_folder)

        with open(f"{test_results_folder}/{file_name}.html", 'w', encoding="utf-8") as file:
            file.write(data)




if __name__ == '__main__':
    unittest.main()
