import os

from webdriver_manager.chrome import ChromeDriverManager


tests_dir = os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(tests_dir)
# CHROME_PATH = os.path.join(PROJ_PATH, 'drivers', 'chromedriver.exe')

CHROME_PATH = ChromeDriverManager().install()

# print('TEST_DIR: ', tests_dir)
# print('PROJ_PATH: ', PROJ_PATH)
# print('CHROME_PATH: ', CHROME_PATH)
