

class device_request:
    device_id = None
    device_model = None
    device_number = None
    monitor_brand = None
    location = None
    software_version = None
    keyboard_brand = None
    tunnel_size=None


    def __init__(self, object):
        if 'device_id' in object:
            self.device_id = object["device_id"]
        if 'tunnel_size' in object:
            self.tunnel_size = object["tunnel_size"]
        if 'device_model' in object:
            self.device_model = object["device_model"]
        if 'device_number' in object:
            self.device_number = object["device_number"]
        if 'monitor_brand' in object:
            self.monitor_brand = object["monitor_brand"]
        if 'location' in object:
            self.location = object["location"]
        if 'software_version' in object:
            self.software_version = object["software_version"]
        if 'keyboard_brand' in object:
            self.keyboard_brand = object["keyboard_brand"]

    def get_device_id(self):
        return self.device_id

    def get_device_model(self):
        return self.device_model
    def get_tunnel_size(self):
        return self.tunnel_size
    def get_device_number(self):
        return self.device_number

    def get_monitor_brand(self):
        return self.monitor_brand

    def get_location(self):
        return self.location

    def get_software_version(self):
        return self.software_version

    def get_keyboard_brand(self):
        return self.keyboard_brand

class Operator_request:
    operator_id = None
    first_name = None
    last_name = None
    company = None
    employee_id = None
    email_address = None
    phone = None
    operator_img = None

    def __init__(self, object):
        if 'operator_id' in object:
            self.operator_id = object["operator_id"]
        if 'first_name' in object:
            self.first_name = object["first_name"]
        if 'last_name' in object:
            self.last_name = object["last_name"]
        if 'company' in object:
            self.company = object["company"]
        if 'phone' in object:
            self.phone = object["phone"]
        if 'employee_id' in object:
            self.employee_id = object["employee_id"]
        if 'email_address' in object:
            self.email_address = object["email_address"]
        if 'operator_img' in object:
            self.operator_img = object["operator_img"]
    def get_operator_id(self):
        return self.operator_id

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name

    def get_company(self):
        return self.company

    def get_phone(self):
        return self.phone

    def get_employee_id(self):
        return self.employee_id

    def get_email_address(self):
        return self.email_address

    def get_operator_img(self):
        return self.operator_img

class ECAC_request:
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
    def __init__(self, object):
        if 'ecac_id' in object:
            self.ecac_id = object["ecac_id"]
        if 'test_view' in object:
            self.test_view = object["test_view"]
        if 'test_date' in object:
            self.test_date = object["test_date"]
        if 'test_time' in object:
            self.test_time = object["test_time"]
        if 'device_id' in object:
            self.device_id = object["device_id"]
        if 'operator_id' in object:
            self.operator_id = object["operator_id"]
        if 'position' in object:
            self.position = object["position"]
        if 'test_1test_2' in object:
            self.test_1test_2 = object["test_1test_2"]
        if 'test_3' in object:
            self.test_3 = object["test_3"]
        if 'test_4a' in object:
            self.test_4a = object["test_4a"]
        if 'test_4b' in object:
            self.test_4b = object["test_4b"]
        if 'test_5' in object:
            self.test_5 = object["test_5"]
    def get_ecac_id(self):
        return self.ecac_id

    def get_test_view(self):
        return self.test_view
    def get_test_date(self):
        return self.test_date

    def get_test_time(self):
        return self.test_time

    def get_device_id(self):
        return self.device_id

    def get_operator_id(self):
        return self.operator_id

    def get_position(self):
        return self.position

    def get_test1_test2(self):
        return self.test_1test_2

    def get_test3(self):
        return self.test_3
    def get_test4a(self):
        return self.test_4a
    def get_test4b(self):
        return self.test_4b
    def get_test5(self):
        return self.test_5



