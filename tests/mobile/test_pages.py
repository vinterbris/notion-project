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
        app.mobile_main_page.press_button_choose_template()
        app.mobile_main_page.choose_template(template_name)

    # THEN
    with step('Шоблон должен быть добавлен'):
        app.mobile_main_page.should_have_reading_list()


def test_search_page():
    app.mobile_login_page.mobile_login(google)

    # WHEN
    app.mobile_main_page.search(default_page)

    # THEN
    app.mobile_main_page.should_have_page(default_page)


def test_delete_page():
    app.mobile_login_page.mobile_login(google)
    app.create_page_from_template(template_name)

    # WHEN
    app.mobile_main_page.open_home()
    app.mobile_main_page.open_home()
    app.mobile_main_page.choose_page_for_deletion()
    app.mobile_main_page.delete_page_on_page_screen()

    # THEN
    app.mobile_main_page.page_should_be_deleted(template_name)
