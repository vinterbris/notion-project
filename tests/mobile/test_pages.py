import pytest
from allure_commons._allure import step

from config import mobile_config
from notion_tests.models.application import app
from notion_tests.test_data.data import template_name, default_page

google = mobile_config.use_google_account_locally


def test_create_page(delete_created_page):
    with step('Логин'):
        app.mobile_login_page.mobile_login(google)

    # WHEN
    with step('Добавить страницу'):
        app.mobile_main_page.add_page()
    with step('Выбрать шаблон'):
        app.mobile.choose_template()

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


@pytest.mark.unstable
def test_delete_page():
    with step('Логин'):
        app.mobile_login_page.mobile_login(google)
    with step('Создать страницу'):
        app.mobile.create_page_from_template(template_name)

    # WHEN
    with step('Открыть домашний экран'):
        app.mobile.open_home()
    with step('Выбрать страницу для удаления'):
        app.mobile_main_page.choose_page_for_deletion()
    with step('Удалить страницу'):
        app.mobile_main_page.delete_page_on_page_screen()

    # THEN
    with step('Страница должна быть удалена'):
        app.mobile_main_page.page_should_be_deleted(template_name)
