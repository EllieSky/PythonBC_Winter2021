import re

import requests
from requests_toolbelt import MultipartEncoder

from tests import DEFAULT_ADMIN_PASSWORD, BASE_URL


class Api:
    def __init__(self):
        self.sess = requests.Session()

    def sign_in(self, username='admin', password=DEFAULT_ADMIN_PASSWORD):
        resp = self.sess.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        result = re.search('value="(.*)" id="csrf_token"', resp.text)
        csrf_token = result.group(1)

        data = f'actionID=&hdnUserTimeZoneOffset=-8&_csrf_token={csrf_token}' + \
               f'&txtUsername={username}&txtPassword={password}&Submit=LOGIN'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        return self.sess.post('http://hrm-online.portnov.com/symfony/web/index.php/auth/validateCredentials',
                  headers=header, data=data)

    def delete_user(self, user_id):
        resp = self.sess.get('http://hrm-online.portnov.com/symfony/web/index.php/admin/viewSystemUsers')
        result = re.search('value="(.*)" id="defaultList__csrf_token"', resp.text)
        csrf_token = result.group(1)

        data = f'defaultList%5B_csrf_token%5D={csrf_token}&chkSelectRow%5B%5D={user_id}'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        return self.sess.post('http://hrm-online.portnov.com/symfony/web/index.php/admin/deleteSystemUsers',
                       headers=header, data=data)

    def add_employee(self, emp_id, first_name, last_name, file=None):
        resp = self.sess.get(f'{BASE_URL}/pim/addEmployee')
        result = re.search('value="(.*)" id="csrf_token"', resp.text)
        csrf_token = result.group(1)

        data = {
            'firstName': first_name,
            'lastName': last_name,
            'employeeId': emp_id,
            'status': 'Enabled',
            'empNumber': emp_id,
            '_csrf_token': csrf_token
        }
        if file:
            data.update({'photofile': ('profile', open(file, 'rb'), 'image/png')})

        mpe = MultipartEncoder(fields=data)

        header = {'Content-Type': mpe.content_type}
        return self.sess.post(f'{BASE_URL}/pim/addEmployee', headers=header, data=mpe.to_string())
