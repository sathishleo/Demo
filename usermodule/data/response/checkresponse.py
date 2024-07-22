import json


class ControlSheet_response:
    id=None
    control_sheet_id =None
    device_id = None
    control_operator_id =None
    check_date = None
    remark = None
    status=None
    signature=None


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_control_sheet_id(self, control_sheet_id):
        self.control_sheet_id = control_sheet_id

    def set_device_id(self, device_id):
        self.device_id = device_id

    def set_control_operator_id(self, control_operator_id):
        self.control_operator_id = control_operator_id

    def set_check_date(self, check_date):
        self.check_date = check_date

    def set_id(self, id):
        self.id = id

    def set_remark(self, remark):
        self.remark = remark
    def set_status(self, status):
        self.status = status


    def set_signature(self, signature):
        self.signature = signature

class CheckRule_response:
    checkrule_id=None
    control_sheet_id = None
    rule_id =None
    rule_choice =None
    remark =None
    status=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_control_sheet_id(self, control_sheet_id):
        self.control_sheet_id = control_sheet_id

    def set_rule_id(self, rule_id):
        self.rule_id = rule_id
    def set_checkrule_id(self, checkrule_id):
        self.checkrule_id = checkrule_id

    def set_rule_choice(self, rule_choice):
        self.rule_choice = rule_choice

    def set_remark(self, remark):
        self.remark = remark
    def set_status(self, status):
        self.status = status