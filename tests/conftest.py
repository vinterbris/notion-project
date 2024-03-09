import os

import pytest
from dotenv import load_dotenv
from selene import browser, have
from selenium.webdriver.chrome.options import Options

from notion_tests.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local",
        choices=["local", "selenoid", "bstack", "mobile_local"],
    )


@pytest.fixture(scope='session', autouse=True)
def load_env(request):
    context = request.config.getoption("--context")
    load_dotenv()
    load_dotenv(dotenv_path=f'.env.{context}')
    print(context)


@pytest.fixture(scope="function", autouse=True)
def attachments():
    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, os.getenv('SELENOID_URL'))


@pytest.fixture(scope="session", autouse=True)
def browser_management(request):
    context = request.config.getoption("--context")
    from config import config

    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height

    options = Options()
    options.page_load_strategy = 'eager'
    browser.config.driver_options = options
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "120.0",
    #     "selenoid:options": {"enableVNC": True, "enableVideo": True},
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    #
    #
    # login = os.getenv("SELENOID_LOGIN")
    # password = os.getenv("SELENOID_PASSWORD")
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options,
    # )
    #
    # browser.config.driver = driver

    yield

    browser.quit()


@pytest.fixture(scope='function')
def delete_current_page():
    yield
    browser.all('[role="treeitem"]')[-1].click()
    browser.element('.notion-topbar-more-button').click()
    browser.all('[role="menuitem"]').element_by(have.text('Delete')).click()
    browser.element('[aria-live="polite"]').should(have.text('Moved to trash'))


@pytest.fixture(scope='function')
def unpublish_page():
    yield
    browser.element('.settings').click()
    browser.all('[role="button"]').element_by(have.text('Unpublish')).click()
    browser.element('.notion-share-menu-publish-button').matching(be.present)
