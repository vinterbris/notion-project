from notion_tests.models.application import app


def test_login():
    google = False

    # WHEN
    app.mobile_login_page.mobile_login(google)

    # THEN
    app.mobile_main_page.ui_elements_should_be_present()
