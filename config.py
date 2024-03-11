import os

import pydantic_settings
from dotenv import load_dotenv

from notion_tests.utils import file

load_dotenv()


class MailConfig(pydantic_settings.BaseSettings):
    mail_wait_timeout: int = 1200000
    mail_api_key: str = os.getenv('MAIL_SLURP_API_KEY')
    mail_inbox_id: str = os.getenv('MAIL_SLURP_INBOX_ID')


class WebConfig(pydantic_settings.BaseSettings):
    timeout: float = 50.0

    notion_api_url: str = os.getenv('API_URL')
    notion_api_key: str = os.getenv('API_KEY')
    notion_id: str = os.getenv('NOTION_PAGE_ID')
    notion_database_id: str = os.getenv('NOTION_DATABASE_ID')

    # web
    base_url: str = os.getenv('URL')
    window_width: int = 1600
    window_height: int = 1000

    def to_driver_options(self, context):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = 'eager'

        if context == 'selenoid':
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": "122.0",
                "selenoid:options": {"enableVNC": True, "enableVideo": True},
            }
            options.capabilities.update(selenoid_capabilities)

        return options


class MobileConfig(pydantic_settings.BaseSettings):
    timeout: float = 15.0
    app: str = os.getenv('APP')
    platform_name: str = os.getenv('BSTACK_PLATFORM_NAME')
    platform_version: str = os.getenv('BSTACK_PLATFORM_VERSION')
    remote_url: str = os.getenv('BSTACK_REMOTE_URL')
    device_name: str = os.getenv('BSTACK_DEVICE_NAME')

    local_app: str = os.getenv('APP')
    local_platform_name: str = os.getenv('PLATFORM_NAME')
    local_remote_url: str = os.getenv('REMOTE_URL')
    local_device_name: str = os.getenv('DEVICE_NAME')

    def to_driver_options(self, context):
        from appium.options.android import UiAutomator2Options
        options = UiAutomator2Options()

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',
                    'userName': os.getenv('BROWSERSTACK_USER_NAME'),
                    'accessKey': os.getenv('BROWSERSTACK_ACCESSKEY'),
                },
            )
        elif context == 'local_mobile':
            options.set_capability('platformName', self.local_platform_name)
            options.set_capability('remote_url', self.local_remote_url)
            options.set_capability('app', file.abs_path_from_project(self.local_app))

        return options


web_config = WebConfig()
mobile_config = MobileConfig()
mail_config = MailConfig()
