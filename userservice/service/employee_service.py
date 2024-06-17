from userservice.data.response.auth_response import emp_response
from userservice.models import Employee


class Emp_service:

    def employee_create(self,object,user_id):
        obj=Employee.objects.create(full_name=object["username"],email=object["email"],user_id=user_id)
        obj.code='EMP'+str(obj.id)
        obj.save()
        Emp_response=emp_response()
        Emp_response.set_id(obj.id)

        Emp_response.set_full_name(obj.full_name)
        return Emp_response

    def get_empid_from_userid(self, user_id):
        employee=None
        if user_id != None:
            employee = Employee.objects.get(user_id=user_id)
            employee_id = employee.id
            return employee_id
        else:
            return employee