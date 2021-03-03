from selenium.webdriver.common.by import By

from base.base import Base


class Table(Base):
    add_btn = (By.ID, 'btnAdd')

    def get_info_from_resultTable_row(self, info, row=1):
        return self.browser.find_element_by_xpath(f'//*[@id="resultTable"]/tbody/tr[{row}]/td[{info}]').text

    def add(self):
        self.browser.find_element(*self.add_btn).click()

    def get_number_of_rows_from_resultTable(self):
        return len(self.browser.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr'))

    def sort_by_column(self, column_name):
        self.browser.find_element(By.XPATH, f"//*[@id='resultTable']//th/a[text()='{column_name}']").click()
