
class GenerateData:
    @staticmethod
    def generate_courier_data(login, password, first_name):
        courier_data = {}
        if login:
            courier_data["login"] = login
        if password:
            courier_data["password"] = password
        if first_name:
            courier_data["firstName"] = first_name
        return courier_data

    @staticmethod
    def generate_order_data(first_name, last_name, station, phone, rent_time, delivery_date, comment, color):
        order_data = {}
        if first_name:
            order_data["firstName"] = first_name
        if last_name:
            order_data["lastName"] = last_name
        if station:
            order_data["metroStation"] = station
        if phone:
            order_data["phone"] = phone
        if rent_time:
            order_data["rentTime"] = rent_time
        if delivery_date:
            order_data["deliveryDate"] = delivery_date
        if comment:
            order_data["comment"] = comment
        if color:
            order_data["color"] = color
        return order_data


