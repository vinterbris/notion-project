import time

import pytest
from selene import browser
from selenium import webdriver

from project import notion_config
from project import web_config
from notion_ui_tests.models.application import app
from notion_ui_tests.test_data.data import workspace_name
from notion_ui_tests.utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_management(request):
    context = notion_config.context

    browser.config.base_url = web_config.base_url
    browser.config.timeout = web_config.timeout
    browser.config.window_width = web_config.window_width
    browser.config.window_height = web_config.window_height

    options = web_config.to_driver_options(context)

    if context == 'remote':
        login = web_config.selenoid_login
        password = web_config.selenoid_password
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options,
        )

        browser.config.driver_options = options
        browser.config.driver = driver
    else:
        browser.config.driver_options = options

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, web_config.selenoid_url)

    time.sleep(5)  # не удаляются страницы из-за быстрого закрытия браузера, поэтому добавил
    browser.quit()


@pytest.fixture(scope='function')
def delete_current_page():
    yield
    app.main_page.topbar.open_page_options_panel()
    app.main_page.page_options.choose_delete()


@pytest.fixture(scope='function')
def unfavorite_and_delete_current_page():
    yield
    app.main_page.topbar.unfavorite_page()
    app.main_page.topbar.open_page_options_panel()
    app.main_page.page_options.choose_delete()


@pytest.fixture(scope='function')
def unpublish_page():
    yield
    app.main_page.share_menu.unpublish_page()


@pytest.fixture(scope='function')
def archive_teamspace():
    yield
    app.main_page.sidebar.archive_teamspace(workspace_name)
