import time

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

    def ui_elements_should_be_present(self):
        self.button_open_home.should(be.present)
        self.button_search.should(be.present)
        self.button_updates.should(
            be.present)
        self.button_add_page.should(be.present)

    def add_page(self):
        self.button_add_page.click()
        # time.sleep(5)
        # self.field_text.click()

    def press_button_choose_template(self):
        time.sleep(5)
        self.field_text.click()
        self.button_choose_template.wait_until(be.visible)
        time.sleep(2)
        self.button_choose_template.click()

    def choose_template(self, value):
        time.sleep(5)
        self.list_of_all_buttons_on_page.element_by(have.text(value)).click()
        self.button_use.click()

    def should_have_reading_list(self):
        time.sleep(5)
        self.reading_list.should(
            be.present)

    def search(self, page):
        self.button_search.click()
        self.field_text.send_keys(page)

    def should_have_page(self, name):
        self.list_of_all_textviews.element_by(have.text(name)).should(be.present)
        self.list_of_all_textviews.element_by(have.text(name)).click()

    def open_home(self):
        time.sleep(5)
        self.button_open_home.click()

    def choose_page_for_deletion(self):
        time.sleep(2)
        self.reading_list_on_home_page.click()

    def delete_page_on_page_screen(self):
        time.sleep(2)
        self.button_page_settings.click()
        self.menuitem_delete.click()

    def page_should_be_deleted(self, name):
        self.list_of_all_textviews.element_by(have.text(name)).should(be.absent)
