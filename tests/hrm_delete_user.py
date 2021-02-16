import json
import os
import re
import unittest

import requests

from tests import PROJ_PATH


class HRM_teardown(unittest.TestCase):
    def test_hrm_api_auth(self):
        session = requests.Session()
        response = session.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        result = re.search('value="(.*)" id="csrf_token"', response.text)
        csrf_token = result.group(1)

        data = f'actionID=&hdnUserTimeZoneOffset=-8&_csrf_token={csrf_token}&txtUsername=admin&txtPassword=password&Submit=LOGIN'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        response2 = session.post('http://hrm-online.portnov.com/symfony/web/index.php/auth/validateCredentials',
                             headers=header, data=data)

        # self.write_to_file(self._testMethodName, response2.text)

        self.assertEqual(200, response2.status_code)
        self.assertTrue(response2.url.endswith('/pim/viewEmployeeList'))
        self.assertIn('Welcome Admin', response2.text)

        # response3 = session.get('http://hrm-online.portnov.com/symfony/web/index.php/pim/getEmployeeListAjax')
        # json_parsed = json.loads(response3.text)
        # self.assertTrue(type(json_parsed) is list)
        # self.assertGreaterEqual(len(json_parsed), 10)
        #
        # names = [i.get('name') for i in json_parsed]
        #
        # self.assertTrue('Admin Admin', names)

        # Adding new ESS Employee

        response4 = session.get('http://hrm-online.portnov.com/symfony/web/index.php/admin/saveSystemUser')
        result4 = re.search('.*" id="systemUser__csrf_token', response4.text)
        print(result4)
        csrf_token = result4.groups(1)
        print('token: ', csrf_token)




    def write_to_file(self, file_name, data):
        test_results_folder = f"{PROJ_PATH}/screenshots"
        if not os.path.exists(test_results_folder):
            os.mkdir(test_results_folder)

        with open(f"{test_results_folder}/{file_name}.html", 'w', encoding="utf-8") as file:
            file.write(data)


if __name__ == '__main__':
    unittest.main()
