import os
from configparser import ConfigParser

from webdriver_manager.chrome import ChromeDriverManager

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(TESTS_DIR)

BROWSER = 'chrome' if not os.environ.get('BROWSER') else os.environ.get('BROWSER').lower()
TEST_ENV = 'default' if not os.environ.get('TEST_ENV') else os.environ.get('TEST_ENV').lower()

config = ConfigParser()
config.read(f'{PROJ_PATH}/config.ini')

DOMAIN = config.get(TEST_ENV, 'DOMAIN')
DEFAULT_WAIT = int(config.get(TEST_ENV, 'DEFAULT_WAIT'))
DEFAULT_ADMIN_PASSWORD = config.get(TEST_ENV, 'DEFAULT_ADMIN_PASSWORD')

CHROME_PATH = ChromeDriverManager().install()
BASE_URL = f'http://{DOMAIN}/symfony/web/index.php'

LONG_WAIT = DEFAULT_WAIT * 3
SHORT_WAIT = int(DEFAULT_WAIT/2)

