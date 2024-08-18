from selene import browser


class StartingPage:

    def __init__(self):
        self.login = browser.element('a[href^="/login"]')

    def open(self):
        browser.open('/')

    def open_login_form(self):
        self.login.click()
