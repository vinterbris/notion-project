from notion_tests.models.application import app
from notion_tests.test_data.data import default_page, template_name


def test_login():
    google = False

    # WHEN
    app.mobile_login_page.mobile_login(google)

    # THEN
    app.mobile_main_page.ui_elements_should_be_present()


def test_create_page(delete_created_page):
    google = True
    app.mobile_login_page.mobile_login(google)

    # WHEN
    app.mobile_main_page.add_page()
    app.mobile_main_page.button_choose_template()
    app.mobile_main_page.choose_template(template_name)

    # THEN
    app.mobile_main_page.should_have_reading_list()


def test_search_page():
    google = True
    app.mobile_login_page.mobile_login(google)

    # WHEN
    app.mobile_main_page.search(default_page)

    # THEN
    app.mobile_main_page.should_have_page(default_page)


# def test_delete_page():
#     google = True
#     app.mobile_login_page.mobile_login(google)
#
#     # WHEN
#     app.mobile_main_page.open_home()
#     app.mobile_main_page.choose_page_for_deletion(template_name)
#     app.mobile_main_page.delete_page()
#
#     # THEN
#     app.mobile_main_page.page_should_be_deleted(template_name)
