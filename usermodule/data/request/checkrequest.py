class ControlSheet_request:
    control_sheet_id =None
    device_id = None
    control_operator_id =None
    check_date = None
    remark = None

    def __init__(self, object):
        if 'control_sheet_id' in object:
            self.control_sheet_id = object["control_sheet_id"]
        if 'device_id' in object:
            self.device_id = object["device_id"]
        if 'check_date' in object:
            self.check_date = object["check_date"]
        if 'remark' in object:
            self.remark = object["remark"]
        if 'control_operator_id' in object:
            self.control_operator_id = object["control_operator_id"]

    def get_control_sheet_id(self):
        return self.control_sheet_id

    def get_device_id(self):
        return self.device_id

    def get_check_date(self):
        return self.check_date

    def get_remark(self):
        return self.remark
    def get_control_operator_id(self):
        return self.control_operator_id

class CheckRule_request:
    checkrule_id=None
    control_sheet_id = None
    rule_id =None
    rule_choice =None
    remark =None
    def __init__(self, object):
        if 'control_sheet_id' in object:
            self.control_sheet_id = object["control_sheet_id"]
        if 'checkrule_id' in object:
            self.control_sheet_id = object["checkrule_id"]
        if 'rule_id' in object:
            self.rule_id = object["rule_id"]
        if 'rule_choice' in object:
            self.rule_choice = object["rule_choice"]
        if 'remark' in object:
            self.remark = object["remark"]

    def get_control_sheet_id(self):
        return self.control_sheet_id

    def get_rule_id(self):
        return self.rule_id
    def get_checkrule_id(self):
        return self.checkrule_id

    def get_rule_choice(self):
        return self.rule_choice

    def get_remark(self):
        return self.remark

class PauseDetails_request:
    pause_details_id=None
    scan_details_id = None
    pause_time = None
    play_time = None
    remarks = None

    def __init__(self, object):
     for i in object:
        if 'pause_details_id' in i:
            self.pause_details_id = i["pause_details_id"]
        if 'scan_details_id' in i:
            self.scan_details_id = i["scan_details_id"]
        if 'pause_time' in i:
            self.pause_time = i["pause_time"]
        if 'play_time' in i:
            self.play_time = i["play_time"]
        if 'remark' in i:
            self.remark = i["remark"]

    def get_scan_details_id_id(self):
        return self.scan_details_id

    def get_pause_details_id(self):
        return self.pause_details_id

    def get_pause_time(self):
        return self.pause_time

    def get_play_time(self):
        return self.play_time

    def get_remark(self):
        return self.remark

