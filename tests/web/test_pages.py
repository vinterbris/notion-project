import allure

from notion_ui_tests.models.application import app
from notion_ui_tests.test_data.data import workspace_name, subpage_name, page_name


@allure.epic('Работа со страницами')
class TestPageFunctions:

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_page(self, delete_current_page):
        app.web.login()

        # WHEN
        app.main_page.sidebar.add_page()

        # THEN
        app.web.should.have_page_fields_and_ui_elements()

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание подстраницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_subpage(self, delete_current_page):
        app.web.login()

        # WHEN
        app.web.add_subpage(subpage_name)

        # THEN
        app.web.should.have_subpage_fields_and_ui_elements(subpage_name)

        app.main_page.open_in_full_page()

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Публикация страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_publish_page(self, unpublish_page):
        app.web.login()

        # WHEN
        published_url = app.web.publish_page()

        # THEN
        app.web.should.be_available(published_url)

    @allure.label('web')
    @allure.epic('Teamspace')
    @allure.feature("Создание teamspace")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_teamspace(self, delete_current_page, archive_teamspace):
        app.web.login()

        # WHEN
        app.web.create_teamspace(workspace_name)

        # THEN
        app.web.should.have_teamspace_ui_elements(workspace_name)

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание страницы из шаблона")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_from_template(self, delete_current_page):
        app.web.login()

        # WHEN
        app.web.create_page_from_template()

        # THEN
        app.web.should.have_table_ui_elements()

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Добавление страницы в избранное")
    @allure.label("owner", "sdobrovolskiy")
    def test_add_page_to_favorites(self, unfavorite_and_delete_current_page):
        app.web.login()

        # WHEN
        app.web.add_page_to_favorites(page_name)

        # THEN
        app.web.should.be_in_favorites(page_name)
