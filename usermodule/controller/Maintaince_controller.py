import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from usermodule.data.request.checkrequest import ControlSheet_request, PauseDetails_request
from usermodule.data.request.devicerequest import device_request
from usermodule.data.request.scanrequest import ScanDetails_request, ShiftDetail_request, DropDown_request, \
    TimeMaintenance_request
from usermodule.service.Maintainance_service import TimeMaintenance_service, PauseDetails_service
from usermodule.service.checksheet_service import Controll_service, scandetails_service, shiftdetails_service, \
    dropdown_service
from usermodule.service.deviceservice import deviceservice, Operator_service, ECAC_service
from userservice.service.employee_service import Emp_service
from utlis.dataservice.demo_authenticate import Authentication
from utlis.dataservice.demo_page import Page_view
from utlis.dataservice.demo_permission import Permission


@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def create_shiftmaintaince(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        TimeMaintenance_data = json.loads(request.body)
        TimeMaintenance_obj = TimeMaintenance_request(TimeMaintenance_data)
        service = TimeMaintenance_service()
        resp_obj = service.create_shiftmaintance(TimeMaintenance_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('limit', 10)
        time_type = request.GET.get('time_type')
        search = request.GET.get('search')

        service = TimeMaintenance_service()
        resp_obj = service.fetch_TimeMaintenance(page_number, per_page, time_type, search)
        # response = HttpResponse(resp_obj.get(), content_type="application/json")
        return resp_obj


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_shiftmaintaince(request, time_maintenance_id):
    if request.method == 'GET':
        service = TimeMaintenance_service()
        resp_obj = service.shiftmaintainance_get(time_maintenance_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = TimeMaintenance_service()
        status = request.GET.get('status')
        Flag = request.GET.get('Flag')
        current_status = request.GET.get('current_status')
        resp_obj = service.modification_shiftmaintainance(time_maintenance_id, status,Flag,current_status)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def create_PauseDetails(request):
    if request.method == 'POST':
        request_obj=None
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        PauseDetails_data = json.loads(request.body)
        if isinstance(PauseDetails_data, list) and all(isinstance(item, dict) for item in PauseDetails_data):
            request_obj = PauseDetails_data
        PauseDetails_obj = PauseDetails_request(PauseDetails_data)
        service = PauseDetails_service()
        resp_obj = service.create_scanmaintance(request_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        scan_details_id = request.GET.get('scan_details_id')
        vys_page = Page_view(page, 10)
        service = PauseDetails_service()
        resp_obj = service.fetch_scanmaintainance(vys_page, scan_details_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_PauseDetails(request, pause_details_id):
    if request.method == 'GET':
        service = PauseDetails_service()
        resp_obj = service.scanmaintainance_get(pause_details_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = PauseDetails_service()
        status = request.GET.get('status')
        Flag = request.GET.get('Flag')
        resp_obj = service.modification_scanmaintainance(status,pause_details_id, Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response