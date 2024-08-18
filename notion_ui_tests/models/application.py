import time

import requests
from allure_commons._allure import step
from selene import be, have

from notion_ui_tests.models.pages.mobile.login_page import MobileLoginPage
from notion_ui_tests.models.pages.mobile.main_page import MobileMainPage
from notion_ui_tests.models.pages.web.login_page import LoginPage
from notion_ui_tests.models.pages.web.main_page import MainPage
from notion_ui_tests.models.pages.web.starting_page import StartingPage


class Application:
    def __init__(self):
        self.starting_page = StartingPage()
        self.login_page = LoginPage()
        self.main_page = MainPage()
        self.mobile_login_page = MobileLoginPage()
        self.mobile_main_page = MobileMainPage()

        # subclasses
        self.web = self.Web(self)
        self.mobile = self.Mobile(self)

    class Web:

        def __init__(self, app):
            self.app = app
            self.should = self.Should(self)

        def login(self):
            with step('Логин'):
                app.starting_page.open()
                if app.login_page.sidebar_switcher.matching(be.absent):
                    app.starting_page.open_login_form()
                    app.login_page.enter_email()
                    app.login_page.enter_code_or_password()
            with step('Закрыть модальное окно, если присутствует'):
                app.main_page.close_modal_window()

        def add_subpage(self, subpage_name):
            with step('Добавить подстраницу'):
                app.main_page.sidebar.add_subpage()
                app.main_page.enter_subpage_name(subpage_name)

        def check_published_page_availability(self, url):
            time.sleep(2)
            response = requests.get(url)
            assert response.status_code == 200

        def publish_page(self):
            with step('Опубликовать страницу'):
                app.main_page.share_menu.open_share_menu()
                app.main_page.share_menu.open_publish_tab()
                app.main_page.share_menu.publish_page()
                return app.main_page.share_menu.get_link()

        def create_teamspace(self, workspace_name):
            with step('Создать teamspace'):
                app.main_page.sidebar.create_teamspace()
                app.main_page.sidebar.name_teamspace(workspace_name)
                app.main_page.sidebar.submit_teamspace()
                app.main_page.sidebar.skip_people_invite()

        def create_page_from_template(self):
            with step('Создать страницу из шаблона'):
                app.main_page.sidebar.open_templates()
                app.main_page.templates_window.choose_todo_list()
                app.main_page.templates_window.get_template()

        def add_page_to_favorites(self, page_name):
            with step('Добавить страницу в избранное'):
                app.main_page.sidebar.add_page()
                app.main_page.enter_page_name(page_name)
                app.main_page.topbar.add_page_to_favorites()

        class Should:

            def __init__(self, web):
                self.web = web

            def have_main_app_ui_elements(self, and_name):
                with step('Должны присутствовать UI элементы страницы'):
                    app.main_page.sidebar.should_have_sidebar_ui_elements(and_name)
                    app.main_page.topbar.should_have_topbar_ui_elements()

            def have_page_fields_and_ui_elements(self):
                with step('Должны быть поля и элементы интерфейса'):
                    app.main_page.should_have_title_field()
                    app.main_page.should_have_top_ui_elements()
                    app.main_page.should_have_bottom_ui_elements()

            def have_subpage_fields_and_ui_elements(self, subpage_name):
                with step('У подстраницы должно быть имя, заголовок, и элементы интерфейса'):
                    app.main_page.sidebar.should_have_title(subpage_name)
                    app.main_page.should_have_title_field()
                    app.main_page.should_have_top_ui_elements()
                    app.main_page.should_have_additional_top_ui_elements()
                    app.main_page.should_have_bottom_ui_elements()

            def be_available(self, published_url):
                with step('Проверить доступность страницы'):
                    self.web.check_published_page_availability(published_url)

            def have_teamspace_ui_elements(self, workspace_name):
                with step('Должны быть элементы интерфейса'):
                    app.main_page.sidebar.should_have_teamspace_ui_elemnts(workspace_name)

            def have_table_ui_elements(self):
                with step('Должно быть имя, таблица, вкладки, кнопки и элементы интерфейса'):
                    app.main_page.sidebar.should_have_title('To-dos')
                    app.main_page.table.should_have_table_view()
                    app.main_page.table.should_have_tabs('Tasks', 'Board')
                    app.main_page.table.should_have_buttons_new(3)
                    app.main_page.table.should_have_buttons()
                    app.main_page.table.should_have_ui_elements()

            def be_in_favorites(self, page_name):
                with step('Проверить, что страница есть в любимых'):
                    app.main_page.sidebar.favorites_should_have_page_with_name(page_name)

    class Mobile:

        def __init__(self, app):
            self.app = app
            self.should = self.Should(self)

        def login(self, google):
            if google:
                with step('Логин через google'):
                    app.mobile_login_page.login_with_google()
            else:
                with step('Логин через почту'):
                    app.mobile_login_page.login_with_email()
            app.mobile_login_page.wait_until_logged_in()
            with step('Разрешить уведомления'):
                app.mobile_login_page.allow_notifications()

        def create_page_from_template(self, name):
            with step('Создать страницу из шаблона'):
                app.mobile_main_page.add_page()
                app.mobile_main_page.press_button_choose_template()
                app.mobile_main_page.choose_template(name)

        def choose_template(self, template_name):
            app.mobile_main_page.press_button_choose_template()
            app.mobile_main_page.choose_template(template_name)

        def find_and_delete_page(self):
            self.open_home()
            with step('На домашнем экране найти и удалить страницу'):
                app.mobile_main_page.choose_page_for_deletion()
                app.mobile_main_page.delete_page_on_page_screen()

        def open_home(self):
            with step('Открыть домашнюю страницу'):
                for _ in range(2):
                    app.mobile_main_page.open_home()

        def search(self, page):
            with step('Найти страницу'):
                app.mobile_main_page.button_search.click()
                app.mobile_main_page.field_text.send_keys(page)

        class Should:

            def __init__(self, mobile):
                self.mobile = mobile

            def have_ui_elements(self):
                with step('Должны присутствовать UI элементы страницы'):
                    app.mobile_main_page.button_open_home.should(be.present)
                    app.mobile_main_page.button_search.should(be.present)
                    app.mobile_main_page.button_updates.should(be.present)
                    app.mobile_main_page.button_add_page.should(be.present)

            def have_reading_list(self):
                with step('Шаблон должен быть добавлен'):
                    app.mobile_main_page.reading_list.wait_until(be.visible)
                    app.mobile_main_page.reading_list.should(be.present)

            def have_page(self, name):
                with step('Страница должна отображаться в результате поиска'):
                    app.mobile_main_page.list_of_all_textviews.element_by(
                        have.text(name)
                    ).should(be.present)
                    app.mobile_main_page.list_of_all_textviews.element_by(
                        have.text(name)
                    ).click()

            def have_no_page(self, name):
                with step('Страница должна быть удалена'):
                    app.mobile_main_page.list_of_all_textviews.element_by(
                        have.text(name)
                    ).should(be.absent)


app = Application()
