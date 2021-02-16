import unittest
import requests


class FoothillBookSearch(unittest.TestCase):
    def test_foothill_booksearch_by_author(self):
        author = 'MOORE'
        url = 'http://books.foothill.edu/postList'
        resp = requests.get(url)
        token = resp.cookies.get('__RequestVerificationToken')
        data = f'__RequestVerificationToken={token}&ClassifiedsName=Owl+Marketplace&AllowPostEditing=True&BookTitle=&BookAuthor={author}&selectedCategory=0&submitButton=Search+Posts'
        resp2 = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data)


        self.assertIn('V FOR VENDETTA', resp2.text)
        self.assertIn('MOORE', resp2.text)
        self.assertIn('978140120841', resp2.text)
        self.assertIn('$13.50', resp2.text)


if __name__ == '__main__':
    unittest.main()