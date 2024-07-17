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


# @swagger_auto_schema(
#     manual_parameters=[
#                           openapi.Parameter('param1', openapi.IN_QUERY, description="Parameter 1",
#                                             type=openapi.TYPE_STRING),
#                           openapi.Parameter('param2', openapi.IN_QUERY, description="Parameter 2",
#                                             type=openapi.TYPE_INTEGER)
#                       ]

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
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get("limit", 10)
        device_model = request.GET.get('device_model')
        search = request.GET.get('search')
        device_number = request.GET.get('device_number')
        tunnel_size = request.GET.get('tunnel_size')
        monitor_brand = request.GET.get('monitor_brand')
        location = request.GET.get('location')
        software_version = request.GET.get('software_version')
        keyboard_brand = request.GET.get('software_version')

        service = deviceservice()
        resp_obj = service.fetch_device( page_number, per_page, device_model,search, device_number, tunnel_size, monitor_brand, location, software_version, keyboard_brand)
        # response = HttpResponse(resp_obj.get(), content_type="application/json")
        return resp_obj

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
        Flag=request.GET.get("Flag")
        resp_obj = service.modification_device(device_id, status,Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

# @csrf_exempt
# @api_view(['GET'])
# # @authentication_classes([Authentication])
# # @permission_classes([IsAuthenticated,Permission])
# def device_search(request):
#     if request.method == 'GET':
#         service = deviceservice()
#         query_text=request.GET.get("query_text")
#         resp_obj = service.fetch_device(query_text)
#         response = HttpResponse(resp_obj.get(), content_type="application/json")
#         return response

@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def operator_create(request):
    if request.method == 'POST':
        operator_data = json.loads(request.data.dict().get('data'))
        file = request.FILES["file"]
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        operator_obj = Operator_request(operator_data)
        opera_service = Operator_service()
        resp_obj = opera_service.create_operator(operator_obj,file)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get("limit", 10)
        first_name = request.GET.get('first_name')
        search = request.GET.get('search')
        operator_id = request.GET.get('operator_id')
        last_name = request.GET.get('last_name')
        company = request.GET.get('company')
        employee_id = request.GET.get('employee_id')
        email_address = request.GET.get('email_address')
        phone = request.GET.get('phone')
        service = Operator_service()
        resp_obj = service.fetch_operator(page_number, per_page, first_name,search,operator_id,last_name,company,employee_id,email_address,phone)
        return resp_obj

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
        Flag=request.GET.get('Flag')
        resp_obj = service.modification_operator(operator_id, status,Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def operator_search(request):
    if request.method == 'GET':
        service = Operator_service()
        query_text=request.GET.get("query_text")
        resp_obj = service.operator_list(query_text)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def download_operator(request):
    if request.method == 'GET':
        name = request.GET.get("gen_key")
        service = ECAC_service()
        resp_obj = service.download_file(name)
        return resp_obj
    
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
        test_view = request.GET.get('test_view')
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get("limit", 10)
        search = request.GET.get("search")
        start_date= request.GET.get("start_date")
        end_date= request.GET.get("end_date")
        start_time= request.GET.get("start_time")
        end_time= request.GET.get("end_time")
        device_id= request.GET.get("device_id")
        tunnel_size= request.GET.get("tunnel_size")
        device_model= request.GET.get("device_model")
        software_version= request.GET.get("software_version")
        operator_id= request.GET.get("operator_id")
        location= request.GET.get("location")
        company= request.GET.get("company")
        position= request.GET.get("position")

        service = ECAC_service()
        resp_obj = service.fetch_ecac(page_number, per_page, test_view,search,start_date,end_date,start_time,end_time,device_id,tunnel_size,device_model,software_version,operator_id,location,company,position)
        return resp_obj

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
        Flag=request.GET.get("Flag")
        resp_obj = service.modification_ecac(ecac_id, status,Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response