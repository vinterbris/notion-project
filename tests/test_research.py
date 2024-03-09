import os

import pyperclip
import requests
from selene import browser, have, be

from notion_tests.utils.verification import get_code_from_email


# UI - 7 test, API - 5 tests, Mobile - 3 tests

# Чисто в теории - можно сделать создание и удаление страницы через api. А на ui автоматизировать что-то другое
# загрузка документа
# создание таблицы
# изменение настроек
# публикация страницы

# TEST Central authentification system (CAS)
def test_login():
    login()

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


def login():
    browser.open('/')
    # WHEN
    browser.element('a[href^="/login"]').click()
    browser.element('#notion-email-input-2').type(os.getenv('LOGIN')).press_enter()
    browser.element('#notion-password-input-1').wait_until(be.visible)
    if browser.all('[role="button"]').element_by(have.text('Continue with login code')).matching(be.present):
        code = get_code_from_email()
        browser.element('#notion-password-input-1').type(code).press_enter()
        if browser.all('.notion-login div').element_by(
                have.text('Your login code was incorrect. Please try again.')).matching(be.present):
            code = get_code_from_email()
            browser.element('#notion-password-input-1').clear().type(code).press_enter()
    else:
        browser.element('#notion-password-input-1').type(os.getenv('PASSWORD')).press_enter()


def login_if_not_logged_in():
    browser.open('/')
    # WHEN
    if browser.element('.notion-sidebar-switcher').matching(be.absent):

        browser.element('a[href^="/login"]').click()
        browser.element('#notion-email-input-2').type(os.getenv('LOGIN')).press_enter()
        browser.element('#notion-password-input-1').wait_until(be.visible)
        if browser.all('[role="button"]').element_by(have.text('Continue with login code')).matching(be.present):
            code = get_code_from_email()
            browser.element('#notion-password-input-1').type(code).press_enter()
            if browser.all('.notion-login div').element_by(
                    have.text('Your login code was incorrect. Please try again.')).matching(be.present):
                code = get_code_from_email()
                browser.element('#notion-password-input-1').clear().type(code).press_enter()
        else:
            browser.element('#notion-password-input-1').type(os.getenv('PASSWORD')).press_enter()


def test_create_page(delete_current_page):
    login_if_not_logged_in()

    # WHEN
    browser.all('[role="button"]').element_by(have.text('Add a page')).click()

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
    login_if_not_logged_in()

    # if browser.all('div').element_by(have.text('This page is in the Trash.')):
    #     browser.all('[role="button"]').element_by(have.text('Add a page')).click()

    # browser.all('.notion-outliner-private .notion-selectable').wait_until(have.size(1))
    browser.element('.notion-topbar-share-menu').click()
    browser.element('.notion-share-menu-publish-tab').click()
    browser.element('.notion-share-menu-publish-button').click()
    browser.element('.link').click()
    browser.element('.globe2').wait_until(be.visible)
    published_url = pyperclip.paste()
    response = requests.get(published_url)
    assert response.status_code == 200


def test_create_from_template(delete_current_page):
    login_if_not_logged_in()
    browser.all('[role="button"]').element_by(have.text('Add a page')).click()
    browser.element('.sidebarTemplates').click()
    browser.element('#tg-simple_tasks').click()
    browser.all('[role="button"]').element_by(have.text('Get template')).click()
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
    login_if_not_logged_in()

    browser.all('[role="button"]').element_by(have.text('Add a page')).click()
    browser.element('[placeholder="Untitled"]').click().type('Favorites test')
    browser.element('.topbarStar').click()
    browser.element('.notion-outliner-bookmarks').should(have.text('Favorites test'))
