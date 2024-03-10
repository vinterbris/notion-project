import os

import requests
from notion_client import Client

from config import web_config

notion = Client(auth=web_config.notion_api_key)


def test_notion():
    # list_users_response = notion.users.list()
    # pprint(list_users_response)

    # response = requests.get('https://cotton-sheet-6c9.notion.site/a8ba44cda9104725ae1dd4325f82de85?pvs=4')
    # pprint(response)

    cookie, cookie_name = get_login_cookie
    with step("Open main page with authorized user"):
        browser.open('/')
        browser.driver.add_cookie({"name": cookie_name, "value": cookie})
        browser.open("/")


def get_login_cookie():
    response = requests.post('' + '/login',
                             data={'Email': os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD'), 'RememberMe': True},
                             allow_redirects=False)
    cookie_name = 'NOPCOMMERCE.AUTH'
    cookie = response.cookies.get(cookie_name)

    yield cookie, cookie_name
