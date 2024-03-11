import os

import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be

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
            browser.driver.execute_script('mobile: hideKeyboard')

            self.enter_password(code)
            self.pressbutton_continue_with_code()

            if self.incorrect_code.matching(be.present):
                code = get_code_from_email()
                self.reenter_code(code)
        self.wait_until_logged_in()
        self.allow_notifications()

    def allow_notifications(self):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
