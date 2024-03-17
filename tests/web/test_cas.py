import allure
from allure_commons._allure import step

from notion_tests.models.application import app


# Баг: иногда при запросе пароля выдает ошибку, что требуется одноразовый код с почты
@allure.label('web')
@allure.epic('Логин')
@allure.label("owner", "sdobrovolskiy")
def test_login():
    # WHEN
    with step('Логин'):
        app.web.login()

    # THEN
    with step('Должны присутствовать UI элементы страницы'):
        app.web.should.have_main_app_ui_elements(and_name="Sergey's Notion")
