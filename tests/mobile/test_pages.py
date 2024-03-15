from allure_commons._allure import step

from config import mobile_config
from notion_tests.models.application import app
from notion_tests.test_data.data import template_name, default_page

google = mobile_config.use_google_account_locally


def test_create_page(delete_created_page):
    with step('Логин'):
        app.mobile_login_page.mobile_login(google)

    # WHEN
    with step('Создать страницу из шаблона'):
        app.mobile.create_page_from_template(template_name)

    # THEN
    with step('Шаблон должен быть добавлен'):
        app.mobile_main_page.should_have_reading_list()


def test_search_page():
    with step('Логин'):
        app.mobile_login_page.mobile_login(google)

    # WHEN
    with step('Найти страницу'):
        app.mobile_main_page.search(default_page)

    # THEN
    with step('Страница должна отображаться в результате поиска'):
        app.mobile_main_page.should_have_page(default_page)


def test_delete_page():
    with step('Логин'):
        app.mobile_login_page.mobile_login(google)
    with step('Создать страницу'):
        app.mobile.create_page_from_template(template_name)

    # WHEN
    with step('На домашнем экране найти и удалить страницу'):
        app.mobile.find_and_delete_page()

    # THEN
    with step('Страница должна быть удалена'):
        app.mobile_main_page.page_should_be_deleted(template_name)
