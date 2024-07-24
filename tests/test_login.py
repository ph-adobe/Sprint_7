import allure
from ya_scooter_api_usage import CourierApiUsage
from data_for_tests import ExpectedResponses as Er


class TestLoginCourier:

    courier = CourierApiUsage()

    @allure.title("Test positive login")
    def test_login_positive(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login(login, password)
        assert status_code == 200
        assert response.get("id")

    @allure.title("Test login without login")
    def test_login_without_login(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login(login,  "")
        assert status_code == 400
        assert response["message"] == Er.message_incomplete_login_data

    @allure.title("Test login without password")
    def test_login_without_password(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login("",  password)
        assert status_code == 400
        assert response["message"] == Er.message_incomplete_login_data

    @allure.title("Test login with incorrect login")
    def test_login_with_incorrect_login(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login(login[::-1], password)
        assert status_code == 404
        assert response["message"] == Er.message_account_not_found

    @allure.title("Test login with incorrect password")
    def test_login_with_incorrect_password(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login(login, password[::-1])
        assert status_code == 404
        assert response["message"] == Er.message_account_not_found

