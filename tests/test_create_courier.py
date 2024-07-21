import allure
import pytest

from ya_scooter_api_usage import CourierApiUsage
from test_data import TestCourierData as Td

class TestCreateCourier:
    url = "https://qa-scooter.praktikum-services.ru"
    path = "/api/v1/courier"

    expected_response_201 = {"ok": True}

    message_incomplete_data = "Недостаточно данных для создания учетной записи"

    message_existing_login = "Этот логин уже используется. Попробуйте другой."

    courier = CourierApiUsage()

    @allure.title("Test courier registration with complete data")
    def test_create_courier_positive(self, successful_registration_data):
        status_code, response = self.courier.register_courier(successful_registration_data)
        assert status_code == 201
        assert response == self.expected_response_201

    @allure.title("Test courier registration with incomplete data")
    @pytest.mark.parametrize(
        "payload",
        [Td.registration_data_wo_login, Td.registration_data_wo_password]
    )
    def test_create_courier_incomplete_data(self, payload):
        status_code, response = self.courier.register_courier(payload)
        assert status_code == 400
        assert response["message"] == self.message_incomplete_data

    @allure.title("Test courier registration with the existing login")
    def test_create_courier_same_login(self, same_user_registration_data):
        status_code, response = self.courier.register_courier(same_user_registration_data)
        assert status_code == 409
        assert response["message"] == self.message_existing_login
