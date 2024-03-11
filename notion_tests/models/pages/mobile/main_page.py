import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MobileMainPage:

    def ui_elements_should_be_present(self):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_home"]')).should(be.present)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_search"]')).should(be.present)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_allUpdates"]')).should(
            be.present)
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).should(be.present)

    def add_page(self):
        browser.element((AppiumBy.XPATH, '//android.view.View[@resource-id="navigate_to_addPage"]')).click()
        time.sleep(5)
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).click()

    def button_choose_template(self):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).click()
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(
            have.text('Choose a template...')).wait_until(
            be.visible)
        time.sleep(2)
        browser.all((AppiumBy.XPATH, '//android.widget.TextView')).element_by(have.text('Choose a template...')).click()

    def choose_template(self, value):
        time.sleep(5)
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text(value)).click()
        browser.all((AppiumBy.XPATH, '//android.widget.Button')).element_by(have.text('Use')).click()

    def should_have_reading_list(self):
        time.sleep(5)
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
        time.sleep(5)
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
