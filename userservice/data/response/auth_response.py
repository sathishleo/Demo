import json


class user_response:
    id=None
    user=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_user(self, user):
        self.user = user

class emp_response:
    id=None
    full_name=None
    user_id=None
    name=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_user_id(self, user_id):
        self.user_id = user_id
