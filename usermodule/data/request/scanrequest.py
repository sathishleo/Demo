class ScanDetails_request:
    scan_details_id = None
    device_id = None
    operator_id = None
    scan_date =None
    start_time = None
    end_time = None
    operator_signature = None
    remark = None
    shift_details_id = None

    def __init__(self, object):
        if 'scan_details_id' in object:
            self.scan_details_id = object["scan_details_id"]
        if 'remark' in object:
            self.remark = object["remark"]
        if 'device_id' in object:
            self.device_id = object["device_id"]
        if 'operator_id' in object:
            self.operator_id = object["operator_id"]
        if 'scan_date' in object:
            self.scan_date = object["scan_date"]
        if 'start_time' in object:
            self.start_time = object["start_time"]
        if 'end_time' in object:
            self.end_time = object["end_time"]
        if 'operator_signature' in object:
            self.operator_signature = object["operator_signature"]
        if 'shift_details_id' in object:
            self.shift_details_id = object["shift_details_id"]

    def get_scan_details_id(self):
        return self.scan_details_id

    def get_device_id(self):
        return self.device_id
    def get_operator_id(self):
        return self.operator_id

    def get_scan_date(self):
        return self.scan_date

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_operator_signature(self):
        return self.operator_signature

    def get_shift_details_id(self):
        return self.shift_details_id
    def get_remark(self):
        return self.remark

class ShiftDetail_request:
    shift_details_id =None
    shift_date = None
    start_time =None
    end_time = None
    scan_count = None
    supervisor = None
    supervisor_signature =None
    remark = None
    status = None

    def __init__(self, object):
        if 'shift_details_id' in object:
            self.shift_details_id = object["shift_details_id"]
        if 'shift_date' in object:
            self.shift_date = object["shift_date"]
        if 'supervisor' in object:
            self.supervisor = object["supervisor"]
        if 'scan_date' in object:
            self.scan_date = object["scan_date"]
        if 'start_time' in object:
            self.start_time = object["start_time"]
        if 'end_time' in object:
            self.end_time = object["end_time"]
        if 'scan_count' in object:
            self.scan_count = object["scan_count"]
        if 'remark' in object:
            self.remark = object["remark"]

    def get_shift_details_id(self):
        return self.shift_details_id

    def get_supervisor(self):
        return self.supervisor

    def get_scan_date(self):
        return self.scan_date


    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_remark(self):
        return self.remark
    def get_scan_count(self):
        return self.scan_count


    def get_shift_date(self):
        return self.shift_date

class DropDown_request:
    drop_down_id=None
    list_item =None
    list_type = None
    status = None

    def __init__(self, object):
        if 'list_item' in object:
            self.list_item = object["list_item"]
        if 'drop_down_id' in object:
            self.drop_down_id = object["drop_down_id"]
        if 'list_type' in object:
            self.list_type = object["list_type"]

    def get_list_item(self):
        return self.list_item
    def get_drop_down_id(self):
        return self.drop_down_id

    def get_list_type(self):
        return self.list_type

class TimeMaintenance_request:
    time_maintenance_id=None
    time_type = None
    decided_minutes =None
    change_date = None
    current_status = None

    def __init__(self, object):
        if 'time_maintenance_id' in object:
            self.time_maintenance_id = object["time_maintenance_id"]
        if 'time_type' in object:
            self.time_type = object["time_type"]
        if 'change_date' in object:
            self.change_date = object["change_date"]
        if 'decided_minutes' in object:
            self.decided_minutes = object["decided_minutes"]
        if 'current_status' in object:
            self.current_status = object["current_status"]

    def get_change_date(self):
        return self.change_date

    def get_time_type(self):
        return self.time_type


    def get_decided_minutes(self):
        return self.decided_minutes

    def get_current_status(self):
        return self.current_status
    def get_time_maintenance_id(self):
        return self.time_maintenance_id
