import json
import requests

HOST = "https://qa-scooter.praktikum-services.ru"


class CourierApiUsage:
    registration_path = "/api/v1/courier"
    login_path = "/api/v1/courier/login"
    delete_path = "/api/v1/courier/:id"

    def register_courier(self, registration_data):
        payload = json.dumps(registration_data)
        response = requests.post(f"{HOST}/{self.registration_path}", data=payload,
                                 headers={"Content-type": "application/json"})
        return response.status_code, response.json()

    def login(self, login, password):
        login_data = {
            "login": login,
            "password": password,
        }

        payload = json.dumps(login_data)
        response = requests.post(f"{HOST}/{self.login_path}", data=payload,
                                 headers={"Content-type": "application/json"})
        return response.status_code, response.json()

    def delete_courier(self, login, password):
        status_code, login_response = self.login(login, password)
        if status_code == 200:
            payload = json.dumps({"id": login_response["id"]})
            response = requests.delete(f"{HOST}/{self.delete_path.replace(':id', str(login_response['id']))}",
                                       data=payload,
                                       headers={"Content-type": "application/json"})
            return response.json()
        else:
            return ("Что-то пошло не так, не удалось получить id пользователя. Пользователь не может быть удален.")


class OrderApiUsage:
    order_list_path = "/api/v1/orders"
    make_order_path = "/api/v1/orders"

    def make_order(self, order_data):
        payload = json.dumps(order_data)
        response = requests.post(f"{HOST}/{self.make_order_path}", data=payload,
                                 headers={"Content-type": "application/json"})
        return response.status_code, response.json()

    def get_orders(self):
        response = requests.get(f"{HOST}/{self.order_list_path}")
        return response.status_code, response.json()

    def get_orders_with_params(self, courier_id=None, nearest_station=None, limit=None, page=None):
        payload = {}
        if courier_id:
            payload["courier_id"] = courier_id
        if nearest_station:
            payload["nearestStation"] = nearest_station
        if limit:
            payload["limit"] = limit
        if page:
            payload["page"] = page
        response = requests.get(f"{HOST}/{self.order_list_path}", params=payload)
        return response.status_code, response.json()
