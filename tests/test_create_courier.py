import allure
import pytest

from ya_scooter_api_usage import CourierApiUsage
from data_for_tests import GeneratedCourierData as Cd, ExpectedResponses as Er


class TestCreateCourier:

    courier = CourierApiUsage()

    @allure.title("Test courier registration with complete data")
    def test_create_courier_positive(self, registration_data):
        status_code, response = self.courier.register_courier(registration_data)
        assert status_code == 201
        assert response == Er.expected_response_201

    @allure.title("Test courier registration with incomplete data")
    @pytest.mark.parametrize(
        "payload",
        [Cd.registration_data_wo_login, Cd.registration_data_wo_password]
    )
    def test_create_courier_incomplete_data(self, payload):
        status_code, response = self.courier.register_courier(payload)
        assert status_code == 400
        assert response["message"] == Er.message_incomplete_registration_data

    @allure.title("Test courier registration with the existing login")
    def test_create_courier_same_login(self, registration_data):
        self.courier.register_courier(registration_data)
        status_code, response = self.courier.register_courier(registration_data)
        assert status_code == 409
        assert response["message"] == Er.message_existing_login
