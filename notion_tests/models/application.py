import requests
import time
from selene import be

from notion_tests.models.pages.mobile.login_page import MobileLoginPage
from notion_tests.models.pages.mobile.main_page import MobileMainPage
from notion_tests.models.pages.web.login_page import LoginPage
from notion_tests.models.pages.web.main_page import MainPage
from notion_tests.models.pages.web.starting_page import StartingPage


class Application:
    def __init__(self):
        self.starting_page = StartingPage()
        self.login_page = LoginPage()
        self.main_page = MainPage()
        self.mobile_login_page = MobileLoginPage()
        self.mobile_main_page = MobileMainPage()

        # self.hide_keyboard = browser.driver.execute_script('mobile: hideKeyboard')

    def login(self):
        app.starting_page.open_login_form()
        app.login_page.enter_email()
        app.login_page.enter_code_or_password()

    def login_if_not_logged_in(self):
        if app.login_page.sidebar_switcher.matching(be.absent):
            self.login()

    def check_published_page_availability(self, url):
        time.sleep(2)
        response = requests.get(url)
        assert response.status_code == 200

    def create_page_from_template(self, name):
        app.mobile_main_page.add_page()
        app.mobile_main_page.press_button_choose_template()
        app.mobile_main_page.choose_template(name)


app = Application()
