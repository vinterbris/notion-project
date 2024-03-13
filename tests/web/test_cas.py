from allure_commons._allure import step

from notion_tests.models.application import app


def test_login():
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login()

    # THEN
    with step('Должны присутствовать UI элементы страницы'):
        app.main_page.sidebar.should_have_sidebar_ui_elements("Sergey's Notion")
        app.main_page.topbar.should_have_topbar_ui_elements()
