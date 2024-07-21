import allure
import pytest
from test_data import TestOrderData as Tod
from ya_scooter_api_usage import OrderApiUsage

order = OrderApiUsage()


class TestMakeOrder:

    @allure.title("Test make order - positive")
    @pytest.mark.parametrize(
        "order_data",
        [Tod.order_full_data_one_color, Tod.order_full_data_both_colors, Tod.order_full_data_wo_colors]
    )
    def test_make_order(self, order_data):
        status_code, response = order.make_order(order_data)
        assert status_code == 201
        assert "track" in response


class TestOrderList:

    @allure.title("Test getting order list without parameters")
    def test_get_orders_wo_params(self):
        status_code, response = order.get_orders()
        assert status_code == 200
        assert response["orders"]

    @allure.title("Test get order list with parameters")
    @pytest.mark.parametrize(
        "params",
        [
            Tod.get_orders_with_all_params,
            Tod.get_orders_with_courier_id,
            Tod.get_orders_with_station,
            Tod.get_orders_with_limit,
            Tod.get_orders_with_page
        ]
    )
    def test_get_orders_with_params(self, params):
        status_code, response = order.get_orders_with_params(*params)
        assert status_code == 200
        assert response["orders"]