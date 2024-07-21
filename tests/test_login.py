import allure
from ya_scooter_api_usage import CourierApiUsage


class TestLoginCourier:
    courier = CourierApiUsage()
    incomplete_data_message = "Недостаточно данных для входа"
    account_not_found_message = "Учетная запись не найдена"

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
        assert response["message"] == self.incomplete_data_message

    @allure.title("Test login without password")
    def test_login_without_password(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login("",  password)
        assert status_code == 400
        assert response["message"] == self.incomplete_data_message

    @allure.title("Test login with incorrect login")
    def test_login_with_incorrect_login(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login(login[::-1], password)
        assert status_code == 404
        assert response["message"] == self.account_not_found_message

    @allure.title("Test login with incorrect password")
    def test_login_with_incorrect_password(self, login_data):
        login, password = login_data
        status_code, response = self.courier.login(login, password[::-1])
        assert status_code == 404
        assert response["message"] == self.account_not_found_message

