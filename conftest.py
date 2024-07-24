import pytest
from data_for_tests import GeneratedCourierData as Cd
from ya_scooter_api_usage import CourierApiUsage


@pytest.fixture
def registration_data():
    registration_data = Cd.generated_complete_data
    yield registration_data
    courier = CourierApiUsage()
    courier.delete_courier(registration_data["login"], registration_data["password"])


@pytest.fixture
def login_data(registration_data):
    courier = CourierApiUsage()
    courier.register_courier(registration_data)
    return registration_data["login"], registration_data["password"]

