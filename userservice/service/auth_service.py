from django.contrib.auth.models import User
from django.http import HttpResponse

from userservice.data.response.auth_response import user_response
from utlis.dataservice.error import Error
from userservice.service.employee_service import Emp_service


class Auth_service:
    def signup(self, obj):
        username_validate = User.objects.filter(username=obj["username"])
        if len(username_validate) != 0:
            response = Error()
            response.set_code("Intergrity Error")
            # response.set_name("Username already existed")
            return response
        else:
            user = User.objects.create_user(username=obj["username"], email=obj["email"], password=obj["password"])
            user_id=user.id
            employee_service = Emp_service()
            employee_response = employee_service.employee_create(obj,user_id)
            response = user_response()
            response.set_id(user.id)
            response.set_user(user.username)
            return response

    def perform_local_auth(self, obj):
        from rest_framework import status
        from django.contrib.auth import authenticate
        from knox.auth import AuthToken
        try:
            username = obj["username"]
            password = obj["password"]
        except KeyError:
            error_data = Error()
            error_data.set_description("invaild request")
            return HttpResponse(error_data.get(), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        print('user', user)
        data = []
        if user is not None:
            token_obj = AuthToken.objects.create(user)
            print(token_obj)
            # auth_data = AuthData()
            auth_user = token_obj[0].user
            token = token_obj[1]
            data.append({"username": auth_user, "token": token})
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)


