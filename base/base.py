from selenium.webdriver.support.wait import WebDriverWait

from tests import DEFAULT_WAIT


class Base(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)
