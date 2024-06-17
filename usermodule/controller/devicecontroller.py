import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from usermodule.data.request.devicerequest import device_request, Operator_request, ECAC_request
from usermodule.service.deviceservice import deviceservice, Operator_service, ECAC_service
from userservice.service.employee_service import Emp_service
from utlis.dataservice.demo_authenticate import Authentication
from utlis.dataservice.demo_page import Page_view
from utlis.dataservice.demo_permission import Permission


@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def device_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        device_data = json.loads(request.body)
        device_obj = device_request(device_data)
        device_service = deviceservice()
        resp_obj = device_service.create_device(device_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        device_model = request.GET.get('device_model')
        vys_page = Page_view(page, 5)
        service = deviceservice()
        resp_obj = service.fetch_device(vys_page, device_model)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_device(request, device_id):
    if request.method == 'GET':
        service = deviceservice()
        resp_obj = service.device_get(device_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = deviceservice()
        status = request.GET.get('status')
        resp_obj = service.modification_device(device_id, status)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def operator_create(request):
    if request.method == 'POST':
        operator_data = json.loads(request.body)
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        operator_obj = Operator_request(operator_data)
        opera_service = Operator_service()
        resp_obj = opera_service.create_operator(operator_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        first_name = request.GET.get('first_name')
        vys_page = Page_view(page, 5)
        service = Operator_service()
        resp_obj = service.fetch_operator(vys_page, first_name)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_operator(request, operator_id):
    if request.method == 'GET':
        service = Operator_service()
        resp_obj = service.operator_get(operator_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = Operator_service()
        status = request.GET.get('status')
        resp_obj = service.modification_operator(operator_id, status)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['POST', 'GET'])
def ecac_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        operator_data = json.loads(request.body)
        operator_obj = ECAC_request(operator_data)
        ecac_service = ECAC_service()
        resp_obj = ecac_service.create_ecac(operator_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        test_view = request.GET.get('test_view')
        vys_page = Page_view(page, 5)
        service = ECAC_service()
        resp_obj = service.fetch_ecac(vys_page, test_view)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_ecac(request, ecac_id):
    if request.method == 'GET':
        service = ECAC_service()
        resp_obj = service.ecac_get(ecac_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = ECAC_service()
        status = request.GET.get('status')
        resp_obj = service.modification_ecac(ecac_id, status)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response