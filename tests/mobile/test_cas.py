from allure_commons._allure import step

from config import mobile_config
from notion_tests.models.application import app


def test_login():
    google = mobile_config.use_google_account_locally

    # WHEN
    with step('Логин'):
        app.mobile_login_page.mobile_login(google)

    # THEN
    with step('Должны присутствовать UI элементы страницы'):
        app.mobile_main_page.ui_elements_should_be_present()
