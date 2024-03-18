import allure

from config import mobile_config
from notion_tests.models.application import app


@allure.label('mobile')
@allure.epic('Логин')
@allure.label("owner", "sdobrovolskiy")
def test_login():
    google = mobile_config.use_google_account_locally

    # WHEN
    app.mobile.login(google)

    # THEN
    app.mobile.should.have_ui_elements()
