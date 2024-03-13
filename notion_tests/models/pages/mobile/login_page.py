import os

import time
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be

from notion_tests.utils.verification import get_code_from_email


class MobileLoginPage:
    def __init__(self):
        self.button_continue_with_password = browser.element(
            ((AppiumBy.XPATH, '//android.widget.Button[@text="Continue with password"]')))
        self.password = browser.element((AppiumBy.XPATH, '//android.view.View[@text="Password"]'))
        self.text_welcome_to_notion_click_to_hide_keyboard = browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Welcome to Notion! 👋"]'))
        self.login_loader = browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Logging in to Notion…'))
        self.google_account_display_name = browser.element(
            (AppiumBy.ID, 'com.google.android.gms:id/account_display_name'))
        self.button_continue_with_login_code = browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(
            have.text('Continue with login code'))
        self.field_password_or_code = browser.all((AppiumBy.CLASS_NAME, 'android.widget.EditText'))[-1]
        self.field_email = browser.element((AppiumBy.XPATH,
                                            '//android.widget.EditText[@resource-id="notion-email-input-2"]'
                                            ))
        self.button_continue_with_email_lowercase = browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="continue with email"]'))
        self.button_continue_with_email = browser.element(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]'))
        self.buton_continue_with_google = browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(
            have.text('Continue with Google'))
        self.incorrect_code = browser.all((AppiumBy.XPATH, 'android.widget.TextView')).element_by(
            have.text('Your login code was incorrect. Please try again.'))
        self.button_continue = browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]'))

    def login_with_google(self):
        self.buton_continue_with_google.click()

    def login_with_email(self):
        self.button_continue_with_email.wait_until(be.visible)
        if self.button_continue_with_email.matching(be.present):
            self.button_continue_with_email.click()
        else:
            self.button_continue_with_email_lowercase.click()

    def enter_email(self):
        self.field_email.type(os.getenv('LOGIN'))

    def press_button_continue(self):
        self.button_continue.click()

    def press_button_login_with_email(self):
        self.button_continue_with_email.click()

    def enter_password(self, code):
        self.field_password_or_code.type(code)

    def press_button_continue_with_code(self):
        self.button_continue_with_login_code.click()

    def reenter_code(self, code):
        self.field_password_or_code.type(code).press_enter()

    def choose_google_user(self):
        self.google_account_display_name.click()

    def wait_until_logged_in(self):
        self.login_loader.wait_until(be.absent)

    def mobile_login(self, google):
        if google:
            self.login_with_google()
            self.choose_google_user()

        else:
            self.login_with_email()
            self.enter_email()

            self.field_password_or_code.wait_until(be.visible)
            if self.button_continue.matching(be.present):
                self.press_button_continue()
            else:
                self.press_button_login_with_email()
            if self.text_welcome_to_notion_click_to_hide_keyboard.matching(be.present):
                self.text_welcome_to_notion_click_to_hide_keyboard.click()
            if self.password.matching(be.present):
                self.enter_password(os.getenv('PASSWORD'))
                self.button_continue_with_password.click()
            else:
                code = get_code_from_email()
                self.enter_password(code)
                self.press_button_continue_with_code()
                if self.incorrect_code.matching(be.present):
                    code = get_code_from_email()
                    self.reenter_code(code)
        self.wait_until_logged_in()
        self.allow_notifications()

    def allow_notifications(self):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
