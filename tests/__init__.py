import os
from webdriver_manager.chrome import ChromeDriverManager

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(TESTS_DIR)
# CHROME_PATH = os.path.join(PROJ_PATH, 'drivers', 'chromedriver')

CHROME_PATH = ChromeDriverManager().install()
DOMAIN = 'hrm-online.portnov.com' if not os.environ.get('DOMAIN') else os.environ.get('DOMAIN')
BASE_URL = f'http://{DOMAIN}/symfony/web/index.php'

DEFAULT_WAIT = 5
LONG_WAIT = DEFAULT_WAIT * 3
SHORT_WAIT = int(DEFAULT_WAIT/2)

DEFAULT_ADMIN_PASSWORD = 'password'
