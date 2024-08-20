import allure

from project import mobile_config
from notion_ui_tests.models.application import app
from notion_ui_tests.test_data.data import template_name, default_page

GOOGLE = mobile_config.use_google_account_locally


@allure.epic('Работа со страницами')
class TestPageFunctions:

    @allure.label('mobile')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_page(self, delete_created_page):
        app.mobile.login(GOOGLE)

        # WHEN
        app.mobile.create_page_from_template(template_name)

        # THEN
        app.mobile.should.have_reading_list()

    @allure.label('mobile')
    @allure.epic('Работа со страницами')
    @allure.feature("Поиск страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_search_page(self):
        app.mobile.login(GOOGLE)

        # WHEN
        app.mobile.search(default_page)

        # THEN
        app.mobile.should.have_page(default_page)

    @allure.label('mobile')
    @allure.epic('Работа со страницами')
    @allure.feature("Удаление страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_delete_page(self):
        app.mobile.login(GOOGLE)
        app.mobile.create_page_from_template(template_name)

        # WHEN
        app.mobile.find_and_delete_page()

        # THEN
        app.mobile.should.have_no_page(template_name)
