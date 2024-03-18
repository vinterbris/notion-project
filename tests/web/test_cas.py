import allure

from notion_tests.models.application import app


# Баг: иногда при запросе пароля выдает ошибку, что требуется одноразовый код с почты
@allure.label('web')
@allure.epic('Логин')
@allure.label("owner", "sdobrovolskiy")
def test_login():
    # WHEN
    app.web.login()

    # THEN
    app.web.should.have_main_app_ui_elements(and_name="Sergey's Notion")
