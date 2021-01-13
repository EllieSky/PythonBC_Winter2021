import os
from webdriver_manager.chrome import ChromeDriverManager

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(TESTS_DIR)

#It will check ChromeDriver version and browser version. It'll install new version if needed.Slower
CHROME_PATH = ChromeDriverManager().install()

#if you whant faster use below, but you need to check versions manually
#CHROME_PATH = os.path.join(PROJ_PATH,'drivers','chromedriver')
