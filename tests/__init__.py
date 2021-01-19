import os

from webdriver_manager.chrome import ChromeDriverManager

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(TESTS_DIR)
CHROME_PATH = os.path.join(PROJ_PATH, 'drivers', 'chromedriver')


#CHROME_PATH = ChromeDriverManager().install()
