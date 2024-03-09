import os

import pyperclip
import requests
import time
from selene import browser, have, be

from notion_tests.utils.verification import get_code_from_email


# UI - 7 test, API - 5 tests, Mobile - 3 tests


class StartingPage:

    def open(self):
        browser.open('/')

    def open_login_form(self):
        browser.element('a[href^="/login"]').click()


class LoginPage:
    def enter_email(self):
        browser.element('#notion-email-input-2').type(os.getenv('LOGIN')).press_enter()
        browser.element('#notion-password-input-1').wait_until(be.visible)

    def enter_code_or_password(self):
        if browser.all('[role="button"]').element_by(have.text('Continue with login code')).matching(be.present):
            code = get_code_from_email()
            browser.element('#notion-password-input-1').type(code).press_enter()
            if browser.all('.notion-login div').element_by(
                    have.text('Your login code was incorrect. Please try again.')).matching(be.present):
                code = get_code_from_email()
                browser.element('#notion-password-input-1').clear().type(code).press_enter()
        else:
            browser.element('#notion-password-input-1').type(os.getenv('PASSWORD')).press_enter()


class MainPage:

    def add_page(self):
        browser.all('[role="button"]').element_by(have.text('Add a page')).click()

    def open_share_menu(self):
        browser.element('.notion-topbar-share-menu').click()

    def open_publish_tab(self):
        browser.element('.notion-share-menu-publish-tab').click()

    def publish_page(self):
        browser.element('.notion-share-menu-publish-button').click()

    def get_link(self):
        browser.element('.link').click()
        browser.element('.globe2').wait_until(be.visible)
        return pyperclip.paste()

    def choose_last_page(self):
        browser.all('[role="treeitem"]')[-1].click()

    def open_page_options_panel(self):
        browser.element('.notion-topbar-more-button').click()

    def choose_delete(self):
        browser.all('[role="menuitem"]').element_by(have.text('Delete')).click()
        browser.all('.notion-outliner-private .notion-selectable').wait_until(have.size(1))

    def unfavorite_page(self):
        browser.element('.topbarStarFilled').click()
        browser.element('.notion-outliner-bookmarks-header-container').matching(be.absent)
        browser.element('.notion-outliner-bookmarks').matching(be.absent)

    def unpublish_page(self):
        browser.all('[role="button"]').element_by(have.text('Unpublish')).click()
        browser.element('.notion-share-menu-publish-button').matching(be.present)
        browser.element('.notion-share-menu-publish-button').press_escape()

    def open_templates(self):
        browser.element('.sidebarTemplates').click()

    def choose_todo_list(self):
        browser.element('#tg-simple_tasks').click()

    def get_template(self):
        browser.all('[role="button"]').element_by(have.text('Get template')).click()

    def enter_page_name(self, name):
        browser.element('[placeholder="Untitled"]').click().type(name)

    def add_page_to_favorites(self):
        browser.element('.topbarStar').click()


class Application:
    def __init__(self):
        self.starting_page = StartingPage()
        self.login_page = LoginPage()
        self.main_page = MainPage()

    def login(self):
        app.starting_page.open_login_form()
        app.login_page.enter_email()
        app.login_page.enter_code_or_password()

    def login_if_not_logged_in(self):
        if browser.element('.notion-sidebar-switcher').matching(be.absent):
            self.login()


app = Application()


# TEST Central authentification system (CAS)
def test_login():
    app.starting_page.open()
    app.login()

    # THEN
    browser.element('.notion-sidebar-switcher').should(have.text("Sergey's Notion"))
    browser.element('.notion-close-sidebar').matching(be.present)
    browser.element('.sidebarSearch').matching(be.present)
    browser.element('.sidebarInbox').matching(be.present)
    browser.element('.sidebarSettings').matching(be.present)
    browser.element('.circlePlus').matching(be.present)
    browser.element('.notion-outliner-private').matching(be.present)
    browser.element('.plusThick').matching(be.present)
    browser.element('.calendarDate09').matching(be.present)
    browser.element('.typesRelation').matching(be.present)
    browser.element('.sidebarInviteTeam').matching(be.present)
    browser.element('.sidebarImport').matching(be.present)
    browser.element('.trash').matching(be.present)

    browser.element('.notion-topbar-share-menu').matching(be.present)
    browser.element('.notion-topbar-comments-button').matching(be.present)
    browser.element('.notion-topbar-updates-button').matching(be.present)
    browser.element('.notion-topbar-favorite-button').matching(be.present)
    browser.element('.notion-topbar-more-button').matching(be.present)


def test_create_page(delete_current_page):
    app.starting_page.open()
    app.login_if_not_logged_in()

    # WHEN
    app.main_page.add_page()

    # THEN
    browser.element('[placeholder="Untitled"]').matching(be.present)
    browser.element('.addPage').matching(be.present)
    browser.element('.addPageCover').matching(be.present)
    browser.element('.addPageDiscussion').matching(be.present)
    browser.element('.sparkles').matching(be.present)
    browser.element('.import').matching(be.present)
    browser.element('.templates').matching(be.present)
    browser.element('.collectionTable').matching(be.present)
    browser.element('.notion-page-content .dots').matching(be.present)


def test_publish_page(unpublish_page):
    app.starting_page.open()
    app.login_if_not_logged_in()

    # WHEN
    app.main_page.open_share_menu()
    app.main_page.open_publish_tab()
    app.main_page.publish_page()
    published_url = app.main_page.get_link()

    # THEN
    time.sleep(2)
    response = requests.get(published_url)
    assert response.status_code == 200


def test_create_from_template(delete_current_page):
    app.starting_page.open()
    app.login_if_not_logged_in()

    # WHEN
    app.main_page.add_page()
    app.main_page.open_templates()
    app.main_page.choose_todo_list()
    app.main_page.get_template()

    # THEN
    browser.all('.notranslate').element_by(have.text('Tasks')).matching(be.present)
    browser.element('.notion-table-view').matching(be.present)
    browser.all('.notion-collection-view-tab-button').should(have.texts('All tasks', 'Board'))
    browser.all('.plus').should(have.size(3))

    browser.all('[role="button"]').element_by(have.text('Filter')).matching(be.present)
    browser.all('[role="button"]').element_by(have.text('Sort')).matching(be.present)
    browser.all('[role="button"]').element_by(have.text('Count')).matching(be.present)

    browser.element('.notion-collection-automation-edit-view').matching(be.present)
    browser.element('.collectionSearch').matching(be.present)
    browser.element('.notion-collection-edit-view').matching(be.present)
    browser.element('.notion-collection-view-item-add').matching(be.present)
    browser.element('.notion-table-view-add-row').matching(be.present)
    browser.element('.typesFormula').matching(be.present)


def test_add_page_to_favorites(unfavorite_and_delete_current_page):
    app.starting_page.open()
    app.login_if_not_logged_in()

    # WHEN
    app.main_page.add_page()
    app.main_page.enter_page_name('Favorites test')
    app.main_page.add_page_to_favorites()

    # THEN
    browser.element('.notion-outliner-bookmarks').should(have.text('Favorites test'))
