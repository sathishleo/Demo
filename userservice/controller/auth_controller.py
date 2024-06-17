import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from userservice.service.auth_service import Auth_service


@csrf_exempt
@api_view(['POST'])
def signup(request):
    # try:
        if request.method=="POST":
            data=json.loads(request.body)
            service=Auth_service()
            # employee_service=Emp_service()
            response=service.signup(data)
            # print(response.id)
            # employee_response=employee_service.employee_create(data,response.id)
            # print(employee_response.get())
            return HttpResponse(response.get(),content_type='application/json')
    # except Exception as e:
    #     print(e)


@csrf_exempt
@api_view(['POST'])
def auth_token(request):
    if request.method=="POST":
        data=json.loads(request.body)
        service=Auth_service()
        response=service.perform_local_auth(data)
        return HttpResponse(response,content_type='application/json')