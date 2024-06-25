import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from usermodule.data.request.checkrequest import ControlSheet_request
from usermodule.data.request.devicerequest import device_request
from usermodule.data.request.scanrequest import ScanDetails_request, ShiftDetail_request, DropDown_request
from usermodule.service.checksheet_service import Controll_service, scandetails_service, shiftdetails_service, \
    dropdown_service, checkrule_service
from usermodule.service.deviceservice import deviceservice, Operator_service, ECAC_service
from userservice.service.employee_service import Emp_service
from utlis.dataservice.demo_authenticate import Authentication
from utlis.dataservice.demo_page import Page_view
from utlis.dataservice.demo_permission import Permission


@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def checksheet_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        checksheet_data=json.loads(request.body)
        checksheet_rule=checksheet_data.get("check_role")
        checksheet_control=checksheet_data.get("controllsheet")

        checksheet_obj = ControlSheet_request(checksheet_control)
        checkrole_obj = ControlSheet_request(checksheet_rule)
        checksheet_service = Controll_service()
        resp_obj = checksheet_service.create_Controll(checksheet_obj)
        service = checkrule_service()
        obj = service.bulk_checkrule(checksheet_rule,resp_obj.control_sheet_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('limit', 10)
        control_operator_id = request.GET.get('control_operator_id')
        search = request.GET.get('search')
        location = request.GET.get('location')
        company = request.GET.get('company')
        device_id = request.GET.get('device_id')
        operator_id = request.GET.get('operator_id')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        service = Controll_service()
        start_date_str=None
        if start_date:
            # Clean the date string from quotes if necessary
            start_date_str = start_date.strip('\'"')

            # Ensure the date string includes default time if missing
            if len(start_date_str) == 10:  # Format: YYYY-MM-DD
                start_date_str += " 00:00:00"
        end_time_str=None
        if end_date:
            # Clean the date string from quotes if necessary
            end_time_str = end_date.strip('\'"')

            # Ensure the date string includes default time if missing
            if len(end_time_str) == 10:  # Format: YYYY-MM-DD
                end_time_str += " 00:00:00"
        resp_obj = service.fetch_Controll(page_number,per_page, control_operator_id,search,location,company,device_id,operator_id,start_date_str,end_time_str)
        # response = HttpResponse(resp_obj.get(), content_type="application/json")
        return resp_obj


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_checksheet(request, control_sheet_id):
    if request.method == 'GET':
        service = Controll_service()
        resp_obj = service.Controll_get(control_sheet_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = Controll_service()
        status = request.GET.get('status')
        resp_obj = service.modification_Controll(control_sheet_id, status)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def checkrole_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # # emp_id = emp_service.get_empid_from_userid(user_id)
        checkrole_data = json.loads(request.body)
        checkrole_obj = ControlSheet_request(checkrole_data)
        checksheet_service = checkrule_service()
        resp_obj = checksheet_service.create_checkrule(checkrole_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        control_operator_id = request.GET.get('control_operator_id')
        vys_page = Page_view(page, 10)
        service = checkrule_service()
        resp_obj = service.fetch_checkrule(vys_page, control_operator_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def child_check_rule(request,control_sheet_id):
    if request.method == 'GET':
        service = checkrule_service()
        resp_obj = service.controllsheet_get(control_sheet_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_checkrole(request, id):
    if request.method == 'GET':
        service = checkrule_service()
        resp_obj = service.checkrule_get(id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = checkrule_service()
        status = request.GET.get('status')
        resp_obj = service.modification_checkrule(id, status)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response


@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def scandetails_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        scandetails_data =json.loads(request.body)
        # img=request.FILES["file"]
        scandetails_obj = ScanDetails_request(scandetails_data)
        Scandetails_service = scandetails_service()
        resp_obj = Scandetails_service.create_scandetails(scandetails_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('limit', 10)
        shift_details = request.GET.get('shift_details')
        search = request.GET.get('search')
        company = request.GET.get('company')
        device_id = request.GET.get('device_id')
        operator_id = request.GET.get('operator_id')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')
        supervisor_name = request.GET.get('supervisor_name')
        service = scandetails_service()
        resp_obj = service.fetch_ScanDetails( page_number, per_page, shift_details, search,company,device_id,operator_id,start_date,end_date,start_time,end_time,supervisor_name)
        # response = HttpResponse(resp_obj.get(), content_type="application/json")
        return resp_obj


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_scandetails(request, scan_details_id):
    if request.method == 'GET':
        service = scandetails_service()
        resp_obj = service.scandetails_get(scan_details_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = scandetails_service()
        status = request.GET.get('status')
        Flag = request.GET.get('Flag')
        resp_obj = service.modification_scandetails(scan_details_id, status,Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def shiftdetails_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        shiftdetails_data =json.loads(request.body)
        # img=request.FILES["file"]
        shiftdetails_obj = ShiftDetail_request(shiftdetails_data)
        Shiftdetails_service = shiftdetails_service()
        resp_obj = Shiftdetails_service.create_shiftdetails(shiftdetails_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get("limit", 10)
        supervisor = request.GET.get('supervisor')
        service = shiftdetails_service()
        resp_obj = service.fetch_shiftdetails(page_number,per_page, supervisor)
        # response = HttpResponse(resp_obj.get(), content_type="application/json")
        return resp_obj


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_shiftdetails(request, shift_details_id):
    if request.method == 'GET':
        service = shiftdetails_service()
        resp_obj = service.shiftdetails_get(shift_details_id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = shiftdetails_service()
        status = request.GET.get('status')
        Flag = request.GET.get('Flag')
        resp_obj = service.modification_shiftdetails(shift_details_id, status,Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

@csrf_exempt
@api_view(['POST', 'GET'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def dropdown_create(request):
    if request.method == 'POST':
        # user_id = request.user.id
        # emp_service = Emp_service()
        # emp_id = emp_service.get_empid_from_userid(user_id)
        DropDown_data = json.loads(request.body)
        DropDown_obj = DropDown_request(DropDown_data)
        service = dropdown_service()
        resp_obj = service.create_dropdown(DropDown_obj)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response

    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page=request.GET.get("limit",10)
        # page = int(page_number)
        list_type = request.GET.get('list_type')
        search = request.GET.get('search')
        # vys_page = Page_view(page, per_page/)
        service = dropdown_service()
        resp_obj = service.fetch_dropdown(page_number,per_page, list_type,search)
        # response = HttpResponse(resp_obj.get(), content_type="application/json")
        return resp_obj


@csrf_exempt
@api_view(['GET', 'DELETE'])
# @authentication_classes([Authentication])
# @permission_classes([IsAuthenticated,Permission])
def view_dropdown(request, id):
    if request.method == 'GET':
        service = dropdown_service()
        resp_obj = service.dropdown_get(id)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response
    elif request.method == 'DELETE':
        service = dropdown_service()
        status = request.GET.get('status')
        Flag=request.GET.get("Flag")
        resp_obj = service.modification_dropdown(id, status,Flag)
        response = HttpResponse(resp_obj.get(), content_type="application/json")
        return response