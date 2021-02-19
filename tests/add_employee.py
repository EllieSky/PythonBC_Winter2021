import unittest

from faker import Faker

from fixtures.fixture import BaseFixture
from menues.user_menu import UserMenu
from pages.add_employee import AddEmployeePage
from pages.employee_info import EmployeeInformationPage
from pages.personal_details import PersonalDetails


class AddEmployee(BaseFixture):
    def test_add_employee_with_credentials(self):
        f = Faker()
        first = f.first_name()
        last = f.last_name()
        self.user_menu = UserMenu(self.browser)
        self.pim_page = EmployeeInformationPage(self.browser)
        self.add_emp_page = AddEmployeePage(self.browser)

        self.login_page.login()

        self.pim_page.wait_for_page_to_load()
        self.pim_page.add()

        emp_id = self.add_emp_page.get_employee_id()
        self.add_emp_page.fill_out_employee_form(
            first, last, None, None, (first, last, emp_id), 'password', 'password')
        self.add_emp_page.save()

        self.personal_details = PersonalDetails(self.browser, emp_id)
        self.personal_details.wait_for_page_to_load()

        self.user_menu.logout()

        self.login_page.login((first, last, emp_id))
        welcome_message = self.user_menu.get_welcome_message()

        self.assertEqual(f"Welcome {first}", welcome_message)


if __name__ == '__main__':
    unittest.main()
