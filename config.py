import os

import dotenv
import pydantic_settings

from notion_tests.utils import file


class NotionConfig(pydantic_settings.BaseSettings):
    context: str = 'local'
    login: str = None
    password: str = None
    api_url: str = 'https://api.notion.co'
    api_key: str = None
    notion_page_id: str = None
    notion_database_id: str = None


class MailConfig(pydantic_settings.BaseSettings):
    '''
    Uses https://www.mailslurp.com/ to generate email and recive login code
    Requires registration, api key and inbox id
    '''

    mail_slurp_api_key: str = None
    mail_slurp_inbox_id: str = None
    mail_wait_timeout: int = 1200000


class WebConfig(pydantic_settings.BaseSettings):
    base_url: str = 'https://www.notion.so'
    timeout: float = 20.0
    window_width: int = 1920
    window_height: int = 1080
    selenoid_url: str = 'selenoid.autotests.cloud'
    selenoid_login: str = None
    selenoid_password: str = None

    def to_driver_options(self, context):
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.page_load_strategy = 'eager'

        if context == 'remote':
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": "122.0",
                "selenoid:options": {"enableVNC": True, "enableVideo": True},
            }
            options.capabilities.update(selenoid_capabilities)

        return options


class MobileConfig(pydantic_settings.BaseSettings):
    timeout: float = 15.0
    use_google_account_locally: bool = os.getenv('USE_GOOGLE')

    application: str = os.getenv('APP_BSTACK')
    platform: str = os.getenv('PLATFORM_NAME_BSTACK')
    platform_ver: str = os.getenv('PLATFORM_VER_BSTACK')
    rem_url: str = os.getenv('REMOTE_URL_BSTACK')
    dev_name: str = os.getenv('DEVICE_NAME_BSTACK')

    local_app: str = os.getenv('APP_LOCAL')
    local_remote_url: str = os.getenv('REMOTE_URL_LOCAL')
    local_platform_name: str = os.getenv('PLATFORM_NAME_LOCAL')

    def to_driver_options(self, context):
        from appium.options.android import UiAutomator2Options

        options = UiAutomator2Options()

        if context == 'remote':
            options.set_capability('remote_url', self.rem_url)
            options.set_capability('deviceName', self.dev_name)
            options.set_capability('platformName', self.platform)
            options.set_capability('platformVersion', self.platform_ver)
            options.set_capability('app', self.application)
            options.set_capability(
                'bstack:options',
                {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',
                    'userName': os.getenv('BROWSERSTACK_USER_NAME'),
                    'accessKey': os.getenv('BROWSERSTACK_ACCESSKEY'),
                },
            )
        elif context == 'local':
            options.set_capability('platformName', self.local_platform_name)
            options.set_capability('remote_url', self.local_remote_url)
            options.set_capability('app', file.abs_path_from_project(self.local_app))

        return options


notion_config = NotionConfig(_env_file=dotenv.find_dotenv('.env'))
mail_config = MailConfig(_env_file=dotenv.find_dotenv('.env.mail'))
web_config = WebConfig(_env_file=dotenv.find_dotenv('.env.web'))
# mobile_config = MobileConfig(_env_file=dotenv.find_dotenv('.env.mobile'))
