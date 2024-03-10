from notion_tests.models.application import app


def test_login():
    app.starting_page.open()
    app.login()

    # THEN
    app.main_page.sidebar.should_have_sidebar_ui_elements("Sergey's Notion")
    app.main_page.topbar.should_have_topbar_ui_elements()