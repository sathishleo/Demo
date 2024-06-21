import json


class device_response:
    device_id = None
    device_model = None
    device_number = None
    monitor_brand = None
    location = None
    software_version = None
    keyboard_brand = None
    status=None
    tunnel_size=None
    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_device_id(self, device_id):
        self.device_id = device_id
    def set_tunnel_size(self, tunnel_size):
        self.tunnel_size = tunnel_size

    def set_device_model(self, device_model):
        self.device_model = device_model

    def set_device_number(self, device_number):
        self.device_number = device_number

    def set_monitor_brand(self, monitor_brand):
        self.monitor_brand = monitor_brand

    def set_location(self, location):
        self.location = location

    def set_software_version(self, software_version):
        self.software_version = software_version

    def set_keyboard_brand(self, keyboard_brand):
        self.keyboard_brand = keyboard_brand
    def set_status(self, status):
        self.status = status

class Operator_response:
    operator_id = None
    first_name = None
    last_name = None
    company = None
    employee_id = None
    email_address = None
    phone = None
    operator_img = None
    status=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_operator_id(self, operator_id):
        self.operator_id = operator_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_company(self, company):
        self.company = company

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def set_email_address(self, email_address):
        self.email_address = email_address

    def set_phone(self, phone):
        self.phone = phone
    def set_status(self, status):
        self.status = status

class ECAC_response:
    ecac_id = None
    test_view = None
    test_date = None
    test_time = None
    device_id = None
    operator_id = None
    position = None
    test_1test_2 = None
    test_3 = None
    test_4a = None
    test_4b = None
    test_5 = None
    status=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_ecac_id(self, ecac_id):
        self.ecac_id = ecac_id

    def set_test_view(self, test_view):
        self.test_view = test_view

    def set_test_date(self, test_date):
        self.test_date = test_date

    def set_test_time(self, test_time):
        self.test_time = test_time

    def set_device_id(self, device_id):
        self.device_id = device_id

    def set_operator_id(self, operator_id):
        self.operator_id = operator_id

    def set_position(self, position):
        self.position = position

    def set_test1_test2(self, test_1test_2):
        self.test_1test_2 = test_1test_2
    def set_test3(self, test3):
        self.test_3 = test3
    def set_test4a(self, test_4a):
        self.test_4a = test_4a
    def set_test4b(self, test_4b):
        self.test_4b = test_4b
    def set_test_5(self, test_5):
        self.test_5 = test_5
    def set_status(self, status):
        self.status = status
