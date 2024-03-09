import requests
import time
from selene import be

from notion_tests.models.pages.web.login_page import LoginPage
from notion_tests.models.pages.web.main_page import MainPage
from notion_tests.models.pages.web.starting_page import StartingPage


class Application:
    def __init__(self):
        self.starting_page = StartingPage()
        self.login_page = LoginPage()
        self.main_page = MainPage()

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


app = Application()
