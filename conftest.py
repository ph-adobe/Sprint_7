import pytest
from test_data import TestCourierData as Td
from ya_scooter_api_usage import CourierApiUsage


@pytest.fixture
def login_data():
    registration_data = Td.generated_complete_data
    courier = CourierApiUsage()
    courier.register_courier(registration_data)
    yield registration_data["login"], registration_data["password"]
    courier.delete_courier(registration_data["login"], registration_data["password"])


@pytest.fixture
def successful_registration_data():
    registration_data = Td.generated_complete_data
    yield registration_data
    courier = CourierApiUsage()
    courier.delete_courier(registration_data["login"], registration_data["password"])


@pytest.fixture
def same_user_registration_data():
    registration_data = Td.generated_complete_data
    courier = CourierApiUsage()
    courier.register_courier(registration_data)
    yield registration_data
    courier.delete_courier(registration_data["login"], registration_data["password"])
