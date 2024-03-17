from allure_commons._allure import step

from notion_tests.models.application import app
from notion_tests.test_data.data import workspace_name, subpage_name, page_name


class TestPageFunctions:

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_page(delete_current_page):
        with step('Логин'):
            app.web.login()

        # WHEN
        with step('Добавить страницу'):
            app.main_page.sidebar.add_page()

        # THEN
        with step('Должны быть поля и элементы интерфейса'):
            app.web.should.have_page_fields_and_ui_elements()

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание подстраницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_subpage(delete_current_page):
        with step('Логин'):
            app.web.login()

        # WHEN
        # Хрупкий шаг из-за hover, при локальном запуске не наводить мышку на браузер
        # Или навести на страницу в сайдбаре, чтобы прошло успешно
        with step('Добавить подстраницу'):
            app.web.add_subpage(subpage_name)

        # THEN
        with step('У подстраницы должно быть имя, заголовок, и элементы интерфейса'):
            app.web.should.have_subpage_fields_and_ui_elements(subpage_name)

        with step('Открыть страницу в полный экран'):
            app.main_page.open_in_full_page()

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Публикация страницы")
    @allure.label("owner", "sdobrovolskiy")
    def test_publish_page(unpublish_page):
        with step('Логин'):
            app.web.login()

        # WHEN
        with step('Опубликовать страницу'):
            published_url = app.web.publish_page()

        # THEN
        with step('Проверить доступность страницы'):
            app.web.should.be_available(published_url)

    @allure.label('web')
    @allure.epic('Teamspace')
    @allure.feature("Создание teamspace")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_teamspace(delete_current_page, archive_teamspace):
        with step('Логин'):
            app.web.login()

        # WHEN
        with step('Создать teamspace'):
            app.web.create_teamspace(workspace_name)

        # THEN
        with step('Должны быть элементы интерфейса'):
            app.web.should.have_teamspace_ui_elements(workspace_name)

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Создание страницы из шаблона")
    @allure.label("owner", "sdobrovolskiy")
    def test_create_from_template(delete_current_page):
        with step('Логин'):
            app.web.login()

        # WHEN
        with step('Создать страницу из шаблона'):
            app.web.create_page_from_template()

        # THEN
        with step('Должно быть имя, таблица, вкладки, кнопки и элементы интерфейса'):
            app.web.should.have_table_ui_elements()

    @allure.label('web')
    @allure.epic('Работа со страницами')
    @allure.feature("Добавление страницы в избранное")
    @allure.label("owner", "sdobrovolskiy")
    def test_add_page_to_favorites(unfavorite_and_delete_current_page):
        with step('Логин'):
            app.web.login()

        # WHEN
        with step('Добавить страницу в избранное'):
            app.web.add_page_to_favorites(page_name)

        # THEN
        with step('Проверить, что страница есть в любимых'):
            app.web.should.be_in_favorites(page_name)
