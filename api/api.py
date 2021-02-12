import re

import requests


class Api:
    def __init__(self):
        self.sess = requests.Session()

    def sign_in(self):
        resp = self.sess.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        result = re.search('value="(.*)" id="csrf_token"', resp.text)
        csrf_token = result.group(1)

        data = f'actionID=&hdnUserTimeZoneOffset=-8&_csrf_token={csrf_token}' + \
               f'&txtUsername=admin&txtPassword=password&Submit=LOGIN'
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
