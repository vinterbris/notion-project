from allure_commons._allure import step

from notion_tests.models.application import app
from notion_tests.test_data.data import workspace_name, subpage_name, page_name


def test_create_page(delete_current_page):
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login_if_not_logged_in()

    # WHEN
    with step('Добавить страницу'):
        app.main_page.sidebar.add_page()

    # THEN
    with step('Должны быть поля и элементы интерфейса'):
        app.main_page.should_have_title_field()
        app.main_page.should_have_top_ui_elements()
        app.main_page.should_have_bottom_ui_elements()


def test_create_subpage(delete_current_page):
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login_if_not_logged_in()

    # WHEN
    with step('Добавить подстраницу'):
        app.main_page.sidebar.add_subpage()
        app.main_page.enter_subpage_name(subpage_name)

    # THEN
    with step('У подстраницы должно быть имя, заголовок, и элементы интерфейса'):
        app.main_page.sidebar.should_have_title(subpage_name)
        app.main_page.should_have_title_field()
        app.main_page.should_have_top_ui_elements()
        app.main_page.should_have_additional_top_ui_elements()
        app.main_page.should_have_bottom_ui_elements()
    with step('Открыть страницу в полный экран'):
        app.main_page.open_in_full_page()


def test_publish_page(unpublish_page):
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login_if_not_logged_in()

    # WHEN
    with step('Открыть меню шаринга'):
        app.main_page.share_menu.open_share_menu()
    with step('Открыть вкладку публикации'):
        app.main_page.share_menu.open_publish_tab()
    with step('Опубликовать страницу'):
        app.main_page.share_menu.publish_page()
    with step('Получить ссылку на страницу'):
        published_url = app.main_page.share_menu.get_link()

    # THEN
    with step('Проверить доступность страницы'):
        app.check_published_page_availability(published_url)


def test_create_teamspace(delete_current_page, archive_teamspace):
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login_if_not_logged_in()

    # WHEN
    with step('Создать тимспейс'):
        app.main_page.sidebar.create_teamspace()
        app.main_page.sidebar.name_teamspace(workspace_name)
        app.main_page.sidebar.submit_teamspace()
    with step('Пропустить добавление людей'):
        app.main_page.sidebar.skip_people_invite()

    # THEN
    with step('Должны быть элементы интерфейса'):
        app.main_page.sidebar.should_have_teamspace_ui_elemnts(workspace_name)


def test_create_from_template(delete_current_page):
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login_if_not_logged_in()

    # WHEN
    with step(''):
        app.main_page.sidebar.open_templates()
    app.main_page.templates_window.choose_todo_list()
    app.main_page.templates_window.get_template()

    # THEN
    with step('Должно быть имя, таблица, вкладки и кнопки new'):
        app.main_page.sidebar.should_have_title('Tasks')
        app.main_page.table.should_have_table_view()
        app.main_page.table.should_have_tabs('All tasks', 'Board')
        app.main_page.table.should_have_buttons_new(3)
    with step('Должны быть кнопки'):
        app.main_page.table.should_have_buttons()
    with step('Должны быть элементы интерфейса'):
        app.main_page.table.should_have_ui_elements()


def test_add_page_to_favorites(unfavorite_and_delete_current_page):
    with step('Открыть сайт'):
        app.starting_page.open()
    with step('Логин'):
        app.login_if_not_logged_in()

    # WHEN
    with step('Создать страницу'):
        app.main_page.sidebar.add_page()
    with step('Назвать страницу'):
        app.main_page.enter_page_name(page_name)
    with step('Добавить страницу в любимые'):
        app.main_page.topbar.add_page_to_favorites()

    # THEN
    with step('Проверить, что страница есть в любимых'):
        app.main_page.sidebar.favorites_should_have_page_with_name(page_name)
