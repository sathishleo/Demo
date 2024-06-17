import json


class SuccessStatus:
    DEFAULT = 'true'
    HTTP = 200
    SUCCESS = 'success'

class SuccessMessage:
    DELETE_MESSAGE = 'Successfully Deleted'
    CREATE_MESSAGE = 'Successfully Created'
    UPDATE_MESSAGE = 'Successfully Updated'
    CLOSED_MESSAGE = 'Successfully Closed'
    SUCCESSFULLY_LOGOUT = 'Successfully logout'
    APPROVED_MESSAGE = 'Approved Successfully'
    REJECTED_MESSAGE = 'Rejected Successfully'
    ACTIVATED='Successfully Activated'
    INACTIVATED='Successfully Inactivated'
    VENDOR_SCHEDULE_EXECUTED_SUCCESSFULLY = 'Vendor Scheduler Executed Successfully'


class Success:
    status = None
    message = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_status(self, status):
        self.status = status

    def set_message(self, message):
        self.message = message