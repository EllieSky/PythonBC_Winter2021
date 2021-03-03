from base.base_page import BasePage


class PersonalDetails(BasePage):
    def __init__(self, browser, emp_number=''):
        super().__init__(browser)
        self.emp_number = emp_number
        # self.page_url = '/pim/viewPersonalDetails/empNumber/' + emp_number
        # self.page_header = 'Personal Details'

    @property
    def page_url(self):
        return '/pim/viewPersonalDetails/empNumber/' + self.emp_number

    @property
    def page_header(self):
        return 'Personal Details'