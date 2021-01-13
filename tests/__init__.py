import os

# here = os.path.abspath(__file__)
from webdriver_manager.chrome import ChromeDriverManager

tests_dir = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(tests_dir)

CHROME_PATH = os.path.join(PROJ_DIR, "Drivers", "chromedriver.exe")

# OR below can be used, but it is slow since its checking the Browser version and driver version (updates if needed)

# CHROME_PATH = ChromeDriverManager().install()
