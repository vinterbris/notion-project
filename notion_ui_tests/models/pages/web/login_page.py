import os

from selene import browser, be, have

from project import notion_config
from notion_ui_tests.utils.verification import get_code_from_email


class LoginPage:
    def __init__(self):
        self.sidebar_switcher = browser.element('.notion-sidebar-switcher')
        self.incorrect_code = browser.all('.notion-login div').element_by(
            have.text('Your login code was incorrect. Please try again.')
        )
        self.button_continue_with_code = browser.all('[role="button"]').element_by(
            have.text('Continue with login code')
        )
        self.password = browser.element('#notion-password-input-1')
        self.email = browser.element('#notion-email-input-2')

    def enter_email(self):
        self.email.type(notion_config.login).press_enter()
        self.password.wait_until(be.visible)

    def enter_code_or_password(self):
        if self.button_continue_with_code.wait_until(be.present):
            code = get_code_from_email()
            self.password.type(code).press_enter()
            if self.incorrect_code.wait_until(be.present):
                code = get_code_from_email()
                self.password.clear().type(code).press_enter()
        else:
            self.password.type(notion_config.password).press_enter()
