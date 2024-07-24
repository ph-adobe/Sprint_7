from helper import GenerateData as Gd
from datetime import date, timedelta
from faker import Faker


class GeneratedCourierData:
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()

    generated_complete_data = Gd.generate_courier_data(login, password, first_name)

    registration_data_wo_login = Gd.generate_courier_data(None, password, first_name)

    registration_data_wo_password = Gd.generate_courier_data(login, None, first_name)


class GeneratedOrderData:
    fake = Faker("ru_RU")

    # Data for making an order
    today = date.today()
    tomorrow = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    both_colors = ["grey", "black"]
    first_name = fake.first_name()
    last_name = fake.last_name()
    station = str(fake.random_int(1, 215))
    phone = fake.phone_number()
    rent_time = fake.random_element(range(1, 6))
    comment = fake.sentence()
    one_color = fake.random_element([["black"], ["grey"]])

    order_full_data_one_color = Gd.generate_order_data(first_name, last_name, station, phone, rent_time, tomorrow,
                                                       comment, one_color)
    order_full_data_both_colors = Gd.generate_order_data(first_name, last_name, station, phone, rent_time, tomorrow,
                                                         comment,
                                                         both_colors)
    order_full_data_wo_colors = Gd.generate_order_data(first_name, last_name, station, phone, rent_time, tomorrow,
                                                       comment, [])
    order_full_data_wo_comment = Gd.generate_order_data(first_name, last_name, station, phone, rent_time, tomorrow,
                                                        None, one_color)

    # Data for getting an order list
    courier_id = fake.random_int(1, 100)
    limit = fake.random_int(1, 30)
    page = fake.random_int(1, 10)

    get_orders_with_all_params = [courier_id, station, limit, page]
    get_orders_with_courier_id = [courier_id]
    get_orders_with_station = [None, station, None, None]
    get_orders_with_limit = [None, None, limit, None]
    get_orders_with_page = [None, None, None, page]


class ExpectedResponses:
    expected_response_201 = {"ok": True}
    message_incomplete_registration_data = "Недостаточно данных для создания учетной записи"
    message_existing_login = "Этот логин уже используется. Попробуйте другой."
    message_incomplete_login_data = "Недостаточно данных для входа"
    message_account_not_found = "Учетная запись не найдена"