
import os

from webdriver_manager.chrome import ChromeDriverManager

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(TEST_DIR)
# CHROME_PATH = os.path.join(PROJ_PATH, 'drivers', 'chromedriver.exe')

CHROME_PATH = ChromeDriverManager().install()