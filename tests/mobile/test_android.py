from notion_tests.models.application import app


def test_login():
    google = False

    # WHEN
    app.mobile_login_page.mobile_login(google)

    # THEN
    app.mobile_main_page.ui_elements_should_be_present()


def test_create_page():
    google = True
    app.mobile_login_page.mobile_login(google)

    # WHEN
    app.mobile_main_page.add_page()
    app.mobile_main_page.button_choose_template()
    app.mobile_main_page.choose_template('Reading List')

    # THEN
    app.mobile_main_page.should_have_reading_list()


def test_search_page():
    google = True
    app.mobile_login_page.mobile_login(google)

    # WHEN
    app.mobile_main_page.search('Getting Started')

    # THEN
    app.mobile_main_page.should_have_page('Getting Started')


def test_delete_page():
    google = True
    app.mobile_login_page.mobile_login(google)

    # WHEN
    app.mobile_main_page.open_home()
    app.mobile_main_page.choose_page_for_deletion('Reading List')
    app.mobile_main_page.delete_page()

    # THEN
    app.mobile_main_page.page_should_be_deleted('Reading List')
