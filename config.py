import dotenv
import pydantic_settings

from notion_ui_tests.utils import file


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
    Uses https://www.mailslurp.com/ to generate email and receive login code
    Requires registration to get api key and inbox id
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

    use_google_account_locally: bool = False

    browserstack_username: str = None
    browserstack_accesskey: str = None

    application_name_bstack: str = None
    platform_name_bstack: str = 'android'
    platform_version_bstack: str = '13.0'
    remote_url_bstack: str = 'http://hub.browserstack.com/wd/hub'
    device_name: str = 'Google Pixel 7'

    local_app: str = None
    local_remote_url: str = 'http://127.0.0.1:4723/wd/hub'
    local_platform_name: str = 'android'

    def to_driver_options(self, context):
        from appium.options.android import UiAutomator2Options

        options = UiAutomator2Options()

        if context == 'remote':
            options.set_capability('remote_url', self.remote_url_bstack)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platform_name_bstack)
            options.set_capability('platformVersion', self.platform_version_bstack)
            options.set_capability('app', self.application_name_bstack)
            options.set_capability(
                'bstack:options',
                {
                    'projectName': 'Notion mobile tests',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack notion testing',
                    'userName': mobile_config.browserstack_username,
                    'accessKey': mobile_config.browserstack_accesskey,
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
mobile_config = MobileConfig(_env_file=dotenv.find_dotenv('.env.mobile'))
