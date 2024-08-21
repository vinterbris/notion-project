import os

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be

from project import notion_config
from notion_ui_tests.utils.verification import get_code_from_email


class MobileLoginPage:
    def __init__(self):
        self.text_temporary_code_sent = browser.element(
            (
                AppiumBy.XPATH,
                '//android.widget.TextView'
                '[@text="We just sent you a temporary login code.\n'
                'Please check your inbox."]',
            )
        )
        self.button_allow_permission = browser.element(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
        )
        self.button_continue_with_password = browser.element(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Continue with password"]')
        )
        self.password = browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Password"]')
        )
        self.text_welcome_to_notion_click_to_hide_keyboard = browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Welcome to Notion! 👋"]')
        )
        self.login_loader = browser.all(
            (AppiumBy.XPATH, '//android.widget.TextView')
        ).element_by(have.text('Logging in to Notion…'))
        self.google_account_display_name = browser.element(
            (AppiumBy.ID, 'com.google.android.gms:id/account_display_name')
        )
        self.button_continue_with_login_code = browser.all(
            (AppiumBy.XPATH, '//android.widget.Button')
        ).element_by(have.text('Continue with login code'))
        self.field_password_or_code = browser.all(
            (AppiumBy.CLASS_NAME, 'android.widget.EditText')
        )[-1]
        self.field_email = browser.element(
            (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="notion-email-input-2"]')
        )
        self.button_continue_with_email_lowercase = browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="continue with email"]')
        )
        self.button_continue_with_email = browser.element(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Continue with email"]')
        )
        self.buton_continue_with_google = browser.all(
            (AppiumBy.XPATH, '//android.widget.Button')
        ).element_by(have.text('Continue with Google'))
        self.incorrect_code = browser.all(
            (AppiumBy.XPATH, 'android.widget.TextView')
        ).element_by(have.text('Your login code was incorrect. Please try again.'))
        self.button_continue = browser.element(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')
        )

    def login_with_google(self):
        self.buton_continue_with_google.click()
        self.google_account_display_name.click()

    def login_with_email(self):
        self.enter_email()
        self.enter_password_or_code()

    def enter_email(self):
        self.button_continue_with_email.wait_until(be.visible)
        self.press_continue()
        self.field_email.type(notion_config.login)
        self.submit_email()

    def submit_email(self):
        try:
            self.button_continue.wait_until(be.present)
        finally:
            if self.button_continue.wait_until(be.present):
                self.press_button_continue()
            else:
                self.press_button_login_with_email()

    def press_continue(self):
        try:
            self.button_continue_with_email_lowercase.wait_until(be.present)
        finally:
            if self.button_continue_with_email_lowercase.wait_until(be.present):
                self.button_continue_with_email_lowercase.click()
            elif self.button_continue_with_email.wait_until(be.present):
                self.button_continue_with_email.click()

    def enter_password_or_code(self):
        try:
            self.text_welcome_to_notion_click_to_hide_keyboard.wait_until(be.present)
            if self.text_welcome_to_notion_click_to_hide_keyboard.wait_until(be.present):
                self.text_welcome_to_notion_click_to_hide_keyboard.click()
        finally:
            if self.text_welcome_to_notion_click_to_hide_keyboard.wait_until(be.present):
                self.text_welcome_to_notion_click_to_hide_keyboard.click()
            elif self.text_temporary_code_sent.wait_until(be.present):
                if self.text_welcome_to_notion_click_to_hide_keyboard.wait_until(be.present):
                    self.text_welcome_to_notion_click_to_hide_keyboard.click()
        self.field_password_or_code.wait_until(be.present)
        if self.password.wait_until(be.present):
            self.enter_password(notion_config.password)
            self.button_continue_with_password.click()
        else:
            code = get_code_from_email()
            self.enter_password(code)
            self.press_button_continue_with_code()
            if self.incorrect_code.wait_until(be.present):
                code = get_code_from_email()
                self.reenter_code(code)

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

    def wait_until_logged_in(self):
        self.login_loader.wait_until(be.absent)

    def allow_notifications(self):
        self.button_allow_permission.click()
