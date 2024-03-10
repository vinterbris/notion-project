import os

import time
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have

from notion_tests.utils.verification import get_code_from_email


def test_login():
    google = True
    if google:
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Continue with Google')).click()
    else:
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text("Continue with email")).click()
        browser.element((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="notion-email-input-2"]')).type(
            os.getenv('LOGIN'))
        if browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Continue')).matching(
                be.present):
            browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Continue')).click()
        else:
            browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(
                have.text('Continue with email')).click()

        code = get_code_from_email()

        browser.driver.execute_script('mobile: hideKeyboard')
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code)
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(
            have.text('Continue with login codel')).click()
        # if self.incorrect_code.matching(be.present):
        #     code = get_code_from_email()
        #     self.password.clear().type(code).press_enter()

    # WHEN
    browser.element((AppiumBy.ID, 'com.google.android.gms:id/account_display_name')).click()
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
        have.text('Logging in to Notion…')).wait_until(be.absent)
    browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()

    # THEN
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_allUpdates"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).should(be.present)


def test_create_page():
    test_login()

    # WHEN
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).click()
    browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Choose a template..."]')).wait_until(be.visible)
    time.sleep(2)
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Choose a template..."]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Reading List"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Use"]')).click()

    # THEN
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Reading List"]')).should(be.present)

def test_search_page():
    test_login()

    # WHEN
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).click()
    # time.sleep(5)
    browser.element((AppiumBy.XPATH, '//android.widget.EditText')).send_keys('Getting Started')

    # THEN
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Getting Started')).should(
        be.present)
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Getting Started')).click()

def test_delete_page():
    test_login()
    time.sleep(2)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).click()
    time.sleep(2)
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).element_by(have.text('Reading List')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[4].click()
    browser.all((AppiumBy.CLASS_NAME, 'android.view.MenuItem')).element_by(have.text('Delete')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Reading List"]')).should(be.absent)

# def test_onboarding():
#     with allure.step('1й экран'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
#             have.text('The Free Encyclopedia\n…in over 300 languages'))
#     with allure.step('2й экран'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
#             have.text('New ways to explore'))
#     with allure.step('3й экран'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
#             have.text('Reading lists with sync'))
#     with allure.step('4й экран'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
#             have.text('Data & Privacy'))
#     with allure.step('Главный экран'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')).should(be.visible)
#
#
# def test_search():
#     with allure.step('Пропустить начальную настройку'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
#     with allure.step('Найти значение'):
#         browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')
#     with allure.step('Подвердить наличие результата поиска'):
#         results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
#         results.should(have.size_greater_than(0))
#         results.first.should(have.text('Appium'))
#
#
# def test_open_article():
#     with allure.step('Пропустить начальную настройку'):
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
#     with allure.step('Найти значение'):
#         browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')
#     with allure.step('Открыть статью'):
#         browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.should(
#             have.text('Appium')).click()
