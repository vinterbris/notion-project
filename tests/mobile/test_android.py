import os

import time
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have

from notion_tests.utils.verification import get_code_from_email


class MobileLoginPage:
    def __init__(self):
        self.incorrect_code = browser.all((AppiumBy.XPATH, 'android.widget.TextView')).element_by(
            have.text('Your login code was incorrect. Please try again.'))
        self.button_continue = browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]'))

    def login_with_google(self):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Continue with Google')).click()

    def login_with_email(self):
        time.sleep(2)
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]')).wait_until(
            be.clickable)
        if browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]')).matching(
                be.present):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]')).click()
        else:
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="continue with email"]')).click()

    def enter_email(self):
        browser.element((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="notion-email-input-2"]'
        )).type(os.getenv('LOGIN'))

    def press_button_continue(self):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')).click()

    def press_button_login_with_email(self):
        browser.all((
            AppiumBy.XPATH,
            '//android.widget.Button'
        )).element_by(have.text('Continue with email')).click()

    def enter_password(self, code):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code)

    def pressbutton_continue_with_code(self):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(
            have.text('Continue with login code')).click()

    def reenter_code(self, code):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1].type(code).press_enter()

    def choose_google_user(self):
        browser.element((AppiumBy.ID, 'com.google.android.gms:id/account_display_name')).click()

    def wait_until_logged_in(self):
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Logging in to Notion…')).wait_until(be.absent)

    def mobile_login(self, google):
        if google:
            self.login_with_google()
            self.choose_google_user()

        else:
            self.login_with_email()
            self.enter_email()

            time.sleep(5)
            if self.button_continue.matching(be.present):
                self.press_button_continue()
            else:
                self.press_button_login_with_email()
            code = get_code_from_email()
            # app.hide_keyboard()
            browser.driver.execute_script('mobile: hideKeyboard')

            mobile_login_page.enter_password(code)
            mobile_login_page.pressbutton_continue_with_code()

            if mobile_login_page.incorrect_code.matching(be.present):
                code = get_code_from_email()
                mobile_login_page.reenter_code(code)
        self.wait_until_logged_in()
        self.allow_notifications()

    def allow_notifications(self):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()


class MobileMainPage:

    def ui_elements_should_be_present(self):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).should(be.present)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).should(be.present)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_allUpdates"]')).should(
            be.present)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).should(be.present)

    def add_page(self):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).click()

    def button_choose_template(self):
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Choose a template...')).wait_until(
            be.visible)
        time.sleep(2)
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Choose a template...')).click()

    def choose_template(self, value):
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text(value)).click()
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Use')).click()

    def should_have_reading_list(self):
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Reading List')).should(
            be.present)

    def search(self, page):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).send_keys(page)

    def should_have_page(self, name):
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text(name)).should(
            be.present)
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text(name)).click()

    def open_home(self):
        time.sleep(2)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).click()

    def choose_page_for_deletion(self, name):
        time.sleep(2)
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).element_by(have.text(name)).click()

    def delete_page(self):
        time.sleep(2)
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[4].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.view.MenuItem')).element_by(have.text('Delete')).click()

    def page_should_be_deleted(self, name):
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text(name)).should(be.absent)


mobile_login_page = MobileLoginPage()
mobile_main_page = MobileMainPage()


def test_login():
    google = False

    # WHEN
    mobile_login_page.mobile_login(google)

    # THEN
    mobile_main_page.ui_elements_should_be_present()


def test_create_page():
    google = True
    mobile_login_page.mobile_login(google)

    # WHEN
    mobile_main_page.add_page()
    mobile_main_page.button_choose_template()
    mobile_main_page.choose_template('Reading List')

    # THEN
    mobile_main_page.should_have_reading_list()


def test_search_page():
    google = True
    mobile_login_page.mobile_login(google)

    # WHEN
    mobile_main_page.search('Getting Started')

    # THEN
    mobile_main_page.should_have_page('Getting Started')


def test_delete_page():
    google = True
    mobile_login_page.mobile_login(google)

    # WHEN
    mobile_main_page.open_home()
    mobile_main_page.choose_page_for_deletion('Reading List')
    mobile_main_page.delete_page()

    # THEN
    mobile_main_page.page_should_be_deleted('Reading List')
