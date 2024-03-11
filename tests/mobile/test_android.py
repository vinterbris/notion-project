import os

import time
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have

from notion_tests.utils.verification import get_code_from_email


class MobileLoginPage:
    def login_with_google(self):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Continue with Google')).click()

    def login_with_email(self):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text("Continue with email")).click()

    def enter_email(self):
        browser.element((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="notion-email-input-2"]'
        )).type(os.getenv('LOGIN'))

    def button_is_continue(self):
        return browser.all((
            AppiumBy.XPATH,
            '//android.widget.Button'
        )).element_by(have.text('Continue')).matching(be.present)

    def press_button_continue(self):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Continue')).click()

    def press_button_login_with_email(self):
        browser.all((
            AppiumBy.XPATH,
            '//android.widget.Button'
        )).element_by(have.text('Continue with email')).click()

    def enter_password(self, code):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code)

    def pressbutton_continue_with_code(self):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(
            have.text('Continue with login codel')).click()

    def incorrect_code(self):
        return browser.all((AppiumBy.XPATH, 'android.widget.TextView')).element_by(
            have.text('Your login code was incorrect. Please try again.')).matching(be.present)

    def reenter_code(self, code):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code).press_enter()

    def mobile_login(self, google):
        if google:
            self.login_with_google()
            browser.element((AppiumBy.ID, 'com.google.android.gms:id/account_display_name')).click()
        else:
            self.login_with_email()
            self.enter_email()

            if self.button_is_continue():
                self.press_button_continue()
            else:
                self.press_button_login_with_email()
            code = get_code_from_email()
            # app.hide_keyboard()
            browser.driver.execute_script('mobile: hideKeyboard')

            mobile_login_page.enter_password(code)
            mobile_login_page.pressbutton_continue_with_code()

            if mobile_login_page.incorrect_code():
                code = get_code_from_email()
                mobile_login_page.reenter_code(code)

        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Logging in to Notion…')).wait_until(be.absent)



class MobileMainPage:
    pass


mobile_login_page = MobileLoginPage()
mobile_main_page = MobileMainPage()


def test_login():
    google = True


    # WHEN
    mobile_login_page.mobile_login(google)
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
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Choose a template...')).wait_until(
        be.visible)
    time.sleep(2)
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Choose a template...')).click()
    browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Reading List')).click()
    browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Use')).click()

    # THEN
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Reading List')).should(be.present)


def test_search_page():
    test_login()

    # WHEN
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.EditText')).send_keys('Getting Started')

    # THEN
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Getting Started')).should(
        be.present)
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Getting Started')).click()


def test_delete_page():
    test_login()

    # WHEN
    time.sleep(2)
    browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).click()
    time.sleep(2)
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).element_by(have.text('Reading List')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[4].click()
    browser.all((AppiumBy.CLASS_NAME, 'android.view.MenuItem')).element_by(have.text('Delete')).click()

    # THEN
    browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Reading List')).should(be.absent)
