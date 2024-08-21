import time

from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MobileMainPage:

    def __init__(self):
        # self.reading_list_on_home_page = browser.element((AppiumBy.XPATH, '(//android.view.View[@resource-id="page_row_Reading List"]/android.view.View/android.view.View[3]'))
        self.reading_list_on_home_page = browser.element(
            (AppiumBy.XPATH, '(//android.widget.TextView[@text="Reading List"])[2]'))
        self.menuitem_delete = browser.all((AppiumBy.CLASS_NAME, 'android.view.MenuItem')).element_by(
            have.text('Delete'))
        self.page_menuitem_delete = browser.all((AppiumBy.XPATH, '//android.widget.TextView[@text="Delete"]'))
        self.button_page_settings = browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button'))[4]
        self.list_of_all_textviews = browser.all((AppiumBy.XPATH, '//android.widget.TextView'))
        self.reading_list = browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Reading List'))
        self.button_use = browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Use'))
        self.list_of_all_buttons_on_page = browser.all((AppiumBy.XPATH, '//android.widget.Button'))
        self.button_choose_template = browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Choose a template...'))
        self.field_text = browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText'))
        self.button_add_page = browser.element(
            (AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]'))
        self.button_updates = browser.element(
            (AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_allUpdates"]'))
        self.button_search = browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]'))
        self.button_open_home = browser.element(
            (AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]'))

    def add_page(self):
        with step('Добавить страницу'):
            self.button_add_page.click()

    def press_button_choose_template(self):
        if self.button_choose_template.wait_until(be.present):
            self.button_choose_template.click()
        else:
            self.field_text.wait_until(be.clickable)
            self.field_text.click()
            self.press_button_choose_template_if_awailable()

    def press_button_choose_template_if_awailable(self):
        if self.button_choose_template.wait_until(be.visible):
            self.button_choose_template.click()

    def choose_template(self, value):
        with step('Выбрать шаблон'):
            self.list_of_all_buttons_on_page.wait_until(be.visible)
            self.list_of_all_buttons_on_page.element_by(have.text(value)).click()
            self.button_use.click()

    def open_home(self):
        self.button_open_home.wait_until(be.visible)
        self.button_open_home.click()

    def choose_page_for_deletion(self):
        self.reading_list_on_home_page.wait_until(be.visible)
        self.reading_list_on_home_page.click()

    def delete_page_on_page_screen(self):
        self.button_page_settings.wait_until(be.visible)
        self.button_page_settings.click()
        self.menuitem_delete.click()
