import os

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, command

from notion_tests.utils.verification import get_code_from_email


def test_login():
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="notion-email-input-2"]')).type(os.getenv('LOGIN'))
    if browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')).matching(be.present):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')).click()
    else:
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]')).click()

    # code = get_code_from_email()
    code = 'nos-qupty-kosta-errim'
    browser.driver.execute_script('mobile: hideKeyboard')
    # browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code)
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code)
    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with login code"]')).click()
    # if self.incorrect_code.matching(be.present):
    #     code = get_code_from_email()
    #     self.password.clear().type(code).press_enter()

    browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()

    # browser.element((AppiumBy.ID, 'navigate_to_home')).should(be.present)
    # browser.element((AppiumBy.ID, 'navigate_to_search')).should(be.present)
    # browser.element((AppiumBy.ID, 'navigate_to_allUpdates')).should(be.present)
    # browser.element((AppiumBy.ID, 'navigate_to_addPage')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_allUpdates"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).should(be.present)

    browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="⚾ Основы"]')).should(be.present)
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Основы"]')).should(be.present)

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
