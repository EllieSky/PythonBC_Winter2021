import json
import os
import re
import time
import unittest

import requests

from api.api import Api
from tests import PROJ_PATH


class HRM_API(unittest.TestCase):
    def test_hrm_api_auth(self):
        sess = requests.Session()
        resp = sess.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        result = re.search('value="(.*)" id="csrf_token"', resp.text)
        csrf_token = result.group(1)

        data = f'actionID=&hdnUserTimeZoneOffset=-8&_csrf_token={csrf_token}&txtUsername=admin&txtPassword=password&Submit=LOGIN'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        resp2 = sess.post('http://hrm-online.portnov.com/symfony/web/index.php/auth/validateCredentials',
                  headers=header, data=data)

        self.write_to_file(self._testMethodName, resp2.text)

        self.assertEqual(200, resp2.status_code)
        self.assertTrue(resp2.url.endswith('/pim/viewEmployeeList'))
        self.assertIn('Welcome Admin', resp2.text)

        resp3 = sess.get('http://hrm-online.portnov.com/symfony/web/index.php/pim/getEmployeeListAjax')
        json_parsed = json.loads(resp3.text)
        self.assertTrue(type(json_parsed) is list)
        self.assertGreaterEqual(len(json_parsed), 10)

        names = [i.get('name') for i in json_parsed]

        self.assertIn('Admin Admin', names)


    def write_to_file(self, file_name, data):
        test_results_folder = f"{PROJ_PATH}/screenshots"
        if not os.path.exists(test_results_folder):
            os.mkdir(test_results_folder)

        with open(f"{test_results_folder}/{file_name}.html", 'w', encoding="utf-8") as file:
            file.write(data)


    def test_hrm_create_employee(self):
        # emp_id = random.randint(10000, 99999)

        emp_id = str(int(time.time() * 100))[-6::]

        api = Api()
        api.sign_in()
        resp = api.add_employee(emp_id, "Billy", "Elliot", file=f'{PROJ_PATH}/empty.png')

        self.write_to_file(self._testMethodName, resp.text)

        self.assertIn('/pim/viewEmployee/empNumber', resp.url)

        emp_number = resp.url.split('/')[-1]



if __name__ == '__main__':
    unittest.main()
