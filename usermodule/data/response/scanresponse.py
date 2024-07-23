import json


class ScanDetails_response:
    scan_details_id = None
    device_id = None
    operator_id = None
    scan_date =None
    start_time = None
    end_time = None
    operator_signature = None
    remark = None
    shift_details_id = None
    status=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_scan_details_id(self, scan_details_id):
        self.scan_details_id = scan_details_id

    def set_device_id(self, device_id):
        self.device_id = device_id

    def set_operator_id(self, operator_id):
        self.operator_id = operator_id

    def set_scan_date(self, scan_date):
        self.scan_date = scan_date

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_remark(self, remark):
        self.remark = remark
    def set_shift_details_id(self, shift_details_id):
        self.shift_details_id = shift_details_id

    def set_status(self, status):
        self.status = status



class ShiftDetail_response:
    shift_details_id =None
    shift_date = None
    start_time =None
    end_time = None
    scan_count = None
    supervisor = None
    supervisor_signature =None
    remark = None
    status = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_shift_details_id(self, shift_details_id):
        self.shift_details_id = shift_details_id

    def set_scan_count(self, scan_count):
        self.scan_count = scan_count

    def set_shift_date(self, shift_date):
        self.shift_date = shift_date

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_remark(self, remark):
        self.remark = remark
    def set_status(self, status):
        self.status = status
    def set_supervisor(self, supervisor):
        self.supervisor = supervisor
    def set_supervisor_signature(self, supervisor_signature):
        self.supervisor_signature = supervisor_signature

class DropDown_response:
    drop_down_id=None
    list_item =None
    list_type = None
    status = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_drop_down_id(self, drop_down_id):
        self.drop_down_id = drop_down_id

    def set_list_item(self, list_item):
        self.list_item = list_item

    def set_list_type(self, list_type):
        self.list_type = list_type

    def set_status(self, status):
        self.status = status

class TimeMaintenance_response:
    time_maintenance_id=None
    time_type = None
    change_date =None
    current_status = None
    decided_minutes = None
    status=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    def set_time_type(self, time_type):
        self.time_type = time_type

    def set_time_maintenance_id(self, time_maintenance_id):
        self.time_maintenance_id = time_maintenance_id
    def set_change_date(self, change_date):
        self.change_date = change_date

    def set_current_status(self, current_status):
        self.current_status = current_status

    def set_decided_minutes(self, decided_minutes):
        self.decided_minutes = decided_minutes

    def set_status(self, status):
        self.status = status


class PauseDetails_response:
    pause_details_id=None
    scan_details_id = None
    pause_time = None
    play_time = None
    remarks = None
    status=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_pause_details_id(self, pause_details_id):
        self.pause_details_id = pause_details_id
    def set_scan_details_id(self, scan_details_id):
        self.scan_details_id = scan_details_id

    def set_pause_time(self, pause_time):
        self.pause_time = pause_time

    def set_play_time(self, play_time):
        self.play_time = play_time

    def set_remarks(self, remarks):
        self.remarks = remarks

    def set_status(self, status):
        self.status = status
