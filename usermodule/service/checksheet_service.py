from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import JsonResponse
from django.utils.timezone import now

from usermodule.data.response.checkresponse import ControlSheet_response, CheckRule_response
from usermodule.data.response.deviceresponse import device_response
from usermodule.data.response.scanresponse import ScanDetails_response, ShiftDetail_response, DropDown_response
from usermodule.models import Device, Operator, ControlSheet, CheckRule, ScanDetails, ShiftDetails, DropDown, \
    TimeMaintenance
from utlis.dataservice.demo_list import Demo_List
from utlis.dataservice.demo_paginator import DemoPaginator
from utlis.dataservice.error import Error
from utlis.dataservice.success import Success, SuccessMessage, SuccessStatus


class Controll_service:

    def create_Controll(self, request_obj,emp_id):
        if request_obj.get_control_sheet_id() is  None:
            Controll_obj = ControlSheet.objects.create(device_id=request_obj.get_device_id(),control_operator_id=request_obj.get_control_operator_id(),check_date=request_obj.get_check_date(),remark=request_obj.get_remark())
        else:
            Controll_obj = ControlSheet.objects.filter(control_sheet_id=request_obj.get_control_sheet_id()).update(device_id=request_obj.get_device_id(),control_operator_id=request_obj.get_control_operator_id(),check_date=request_obj.get_check_date(),remark=request_obj.get_remark(),updated_date=now())
            Controll_obj = ControlSheet.objects.get(control_sheet_id=request_obj.get_control_sheet_id())
        temp_response = ControlSheet_response()
        temp_response.set_device_id(Controll_obj.device_id)
        temp_response.set_control_operator_id(Controll_obj.control_operator)
        temp_response.set_control_sheet_id(Controll_obj.control_sheet_id)
        temp_response.set_check_date(Controll_obj.check_date)
        temp_response.set_remark(Controll_obj.remark)
        return temp_response

    def fetch_Controll(self, vys_page, control_operator_id):
        try:
            condition = Q(status=1)
            if control_operator_id != " " and control_operator_id != None:
                condition &= Q(control_operator_id=control_operator_id)
            obj = ControlSheet.objects.filter(condition)[
                  vys_page.get_offset():vys_page.get_query_limit()]

            list_length = len(obj)
            pro_list = Demo_List()
            if list_length <= 0:
                return pro_list
            else:

                for i in obj:
                    temp_response = ControlSheet_response()
                    temp_response.set_device_id(i.device_id)
                    temp_response.set_control_operator_id(i.control_operator)
                    temp_response.set_control_sheet_id(i.control_sheet_id)
                    temp_response.set_check_date(str(i.check_date))
                    temp_response.set_remark(i.remark)
                    pro_list.append(temp_response)
                vpage = DemoPaginator(obj, vys_page.get_index(), 10)
                pro_list.set_pagination(vpage)
                return pro_list
        except Exception as e:
            error_obj = Error()
            print(e)
            # error_obj.set_code(ErrorMessage.INVALID_DATA)
            error_obj.set_description(str(e))
            return error_obj

    def Controll_get(self, control_sheet_id):
        id_obj = ControlSheet.objects.get(control_sheet_id=control_sheet_id)
        temp_response = ControlSheet_response()
        temp_response.set_device_id(id_obj.device_id)
        temp_response.set_control_operator_id(id_obj.control_operator)
        temp_response.set_control_sheet_id(id_obj.control_sheet_id)
        temp_response.set_check_date(str(id_obj.check_date))
        temp_response.set_remark(id_obj.remark)

        return temp_response

    def modification_Controll(self, status, control_sheet_id):
        modification_obj = ControlSheet.objects.filter(control_sheet_id=control_sheet_id).update(status=status)
        success_obj = Success()
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        success_obj.set_status(SuccessStatus.SUCCESS)
        return success_obj

class checkrule_service:

    def create_checkrule(self, request_obj,emp_id):
        if request_obj.get_icheckrule_id() is  None:
            Controll_obj = CheckRule.objects.create(rule_id=request_obj.get_rule_id(),control_sheet_id=request_obj.get_control_sheet_id(),rule_choice=request_obj.get_rule_choice(),remark=request_obj.get_remark())
        else:
            Controll_obj = CheckRule.objects.filter(checkrule_id=request_obj.get_checkrule_id()).update(rule_id=request_obj.get_rule_id(),control_sheet_id=request_obj.get_control_sheet_id(),rule_choice=request_obj.get_rule_choice(),remark=request_obj.get_remark(),updated_date=now())
            Controll_obj = CheckRule.objects.get(checkrule_id=request_obj.get_checkrule_id())
        temp_response = CheckRule_response()
        temp_response.set_checkrule_id(Controll_obj.checkrule_id)
        temp_response.set_rule_id(Controll_obj.rule_id)
        temp_response.set_control_sheet_id(Controll_obj.control_sheet_id)
        temp_response.set_rule_choice(Controll_obj.rule_choice)
        temp_response.set_remark(Controll_obj.remark)
        return temp_response

    def fetch_checkrule(self, vys_page, control_sheet):
        try:
            condition = Q(status=1)
            if control_sheet != " " and control_sheet != None:
                condition &= Q(control_sheet_id=control_sheet)
            obj = CheckRule.objects.filter(condition)[
                  vys_page.get_offset():vys_page.get_query_limit()]

            list_length = len(obj)
            pro_list = Demo_List()
            if list_length <= 0:
                return pro_list
            else:

                for i in obj:
                    temp_response = CheckRule_response()
                    temp_response.set_checkrule_id(i.checkrule_id)
                    temp_response.set_rule_id(i.rule_id)
                    temp_response.set_control_sheet_id(i.control_sheet_id)
                    temp_response.set_rule_choice(i.rule_choice)
                    temp_response.set_remark(i.remark)

                    pro_list.append(temp_response)
                vpage = DemoPaginator(obj, vys_page.get_index(), 10)
                pro_list.set_pagination(vpage)
                return pro_list
        except Exception as e:
            error_obj = Error()
            print(e)
            # error_obj.set_code(ErrorMessage.INVALID_DATA)
            error_obj.set_description(str(e))
            return error_obj

    def checkrule_get(self, id):
        id_obj = CheckRule.objects.get(checkrule_id=id)
        temp_response = CheckRule_response()
        temp_response.set_rule_choice(id_obj.rule_choice)
        temp_response.set_checkrule_id(id_obj.checkrule_id)
        temp_response.set_rule_id(id_obj.rule_id)
        temp_response.set_control_sheet_id(id_obj.control_sheet_id)
        temp_response.set_remark(id_obj.remark)

        return temp_response

    def modification_checkrule(self, checkrule_id, status):
        modification_obj = CheckRule.objects.filter(checkrule_id=checkrule_id).update(status=status)
        if modification_obj == 0:
            response = Error()
            response.set_code("ID NOT MATCHED")
            # response.set_name("Username already existed")
            return response
        else:
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj


class scandetails_service:

    def create_scandetails(self, request_obj,img):
        # try:
        if request_obj.get_scan_details_id() is  None:
            obj_validation=self.validation_scan(request_obj.get_operator_id())

            if obj_validation==True:
                ScanDetails_obj = ScanDetails.objects.create(device_id=request_obj.get_device_id(),operator_id=request_obj.get_operator_id(),scan_date=request_obj.get_scan_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),shift_details_id=request_obj.get_shift_details_id(),operator_signature=img)
                temp_response = ScanDetails_response()
                temp_response.set_scan_details_id(ScanDetails_obj.scan_details_id)
                temp_response.set_device_id(ScanDetails_obj.device_id)
                temp_response.set_operator_id(ScanDetails_obj.operator_id)
                temp_response.set_scan_date(str(ScanDetails_obj.scan_date))
                temp_response.set_start_time(ScanDetails_obj.start_time)
                temp_response.set_end_time(ScanDetails_obj.end_time)
                return temp_response
            else:
                error=Error()
                error.set_description("vaild break time")
                return error
        else:
            ScanDetails_obj = ScanDetails.objects.filter(scan_details_id=request_obj.get_scan_details_id()).update(device_id=request_obj.get_device_id(),operator_id=request_obj.get_operator_id(),scan_date=request_obj.get_scan_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),shift_details_id=request_obj.get_shift_details_id(),updated_date=now(),operator_signature=img)
            ScanDetails_obj = ScanDetails.objects.get(scan_details_id=request_obj.get_scan_details_id())
        temp_response = ScanDetails_response()
        temp_response.set_scan_details_id(ScanDetails_obj.scan_details_id)
        temp_response.set_device_id(ScanDetails_obj.device_id)
        temp_response.set_operator_id(ScanDetails_obj.operator_id)
        temp_response.set_scan_date(str(ScanDetails_obj.scan_date))
        temp_response.set_start_time(str(ScanDetails_obj.start_time))
        temp_response.set_end_time(str(ScanDetails_obj.end_time))
        return temp_response

    def fetch_scandetails(self, vys_page, shift_details):
        try:
            condition = Q(status=1)
            if shift_details != " " and shift_details != None:
                condition &= Q(shift_details_id=shift_details)
            obj = ScanDetails.objects.filter(condition)[
                  vys_page.get_offset():vys_page.get_query_limit()]

            list_length = len(obj)
            pro_list = Demo_List()
            if list_length <= 0:
                return pro_list
            else:

                for i in obj:
                    temp_response = ScanDetails_response()
                    temp_response.set_scan_details_id(i.scan_details_id)
                    temp_response.set_device_id(i.device_id)
                    temp_response.set_operator_id(i.operator_id)
                    temp_response.set_scan_date(str(i.scan_date))
                    temp_response.set_start_time(str(i.start_time))
                    temp_response.set_end_time(str(i.end_time))
                    temp_response.set_status(i.status)

                    pro_list.append(temp_response)
                vpage = DemoPaginator(obj, vys_page.get_index(), 10)
                pro_list.set_pagination(vpage)
                return pro_list
        except Exception as e:
            error_obj = Error()
            print(e)
            # error_obj.set_code(ErrorMessage.INVALID_DATA)
            error_obj.set_description(str(e))
            return error_obj

    def scandetails_get(self, scan_details_id):
        id_obj = ScanDetails.objects.get(scan_details_id=scan_details_id)
        temp_response = ScanDetails_response()
        temp_response.set_scan_details_id(id_obj.scan_details_id)
        temp_response.set_device_id(id_obj.device_id)
        temp_response.set_operator_id(id_obj.operator_id)
        temp_response.set_scan_date(str(id_obj.scan_date))
        temp_response.set_start_time(str(id_obj.start_time))
        temp_response.set_end_time(str(id_obj.end_time))
        temp_response.set_status(id_obj.status)

        return temp_response

    def modification_scandetails(self, scan_details_id, status):
        modification_obj = ScanDetails.objects.filter(scan_details_id=scan_details_id).update(status=status)
        if modification_obj == 0:
            response = Error()
            response.set_code("ID NOT MATCHED")
            # response.set_name("Username already existed")
            return response
        else:
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj

    def validation_scan(self, operator_id):
    # Retrieve the latest maintenance record created by the employee
        maintenance = ScanDetails.objects.filter(operator_id=operator_id).order_by("-created_date")
        check = False

        if len(maintenance) == 0:
            check = True
        else:
            # Get the desired time duration from TimeMaintenance
            Time_obj = TimeMaintenance.objects.get(time_type=2)
            # Assuming Time_obj has an attribute `desired_minutes` which specifies the allowed time frame in minutes
            allowed_minutes = Time_obj.decided_minutes

            # Get the latest maintenance record's created_date
            latest_maintenance_date = maintenance[0].created_date
            from datetime import timedelta
            from django.utils import timezone
            current_time = timezone.now()

            # Check if the latest maintenance record is within the allowed time frame
            if timezone.is_naive(latest_maintenance_date):
                latest_maintenance_date = timezone.make_aware(latest_maintenance_date, timezone.get_current_timezone())
            if (latest_maintenance_date) + timedelta(minutes=allowed_minutes) > (current_time):
                check = False
            else:
                check = True

        return check


    # def validation_scan(self, emp_id):
    #     # Retrieve the latest maintenance record created by the employee
    #     maintenance = ScanDetails.objects.filter(created_by=emp_id).order_by("-created_date")
    #     check = False
    #
    #     if len(maintenance) == 0:
    #         check = True
    #     else:
    #         # Get the desired time duration from TimeMaintenance
    #         Time_obj = TimeMaintenance.objects.get(time_type=2)
    #         # Assuming Time_obj has an attribute `desired_minutes` which specifies the allowed time frame in minutes
    #         allowed_minutes = Time_obj.decided_minutes
    #
    #         # Get the latest maintenance record's created_date
    #         latest_maintenance_date = maintenance[0].created_date
    #         from datetime import timedelta
    #         from django.utils import timezone
    #         current_time = timezone.now()
    #
    #         # Check if the latest maintenance record is within the allowed time frame
    #         if timezone.is_naive(latest_maintenance_date):
    #             latest_maintenance_date = timezone.make_aware(latest_maintenance_date, timezone.get_current_timezone())
    #         if (latest_maintenance_date) + timedelta(minutes=allowed_minutes) > (current_time):
    #             check = False
    #         else:
    #             check = True
    #
    #     return check
class shiftdetails_service:

    def create_shiftdetails(self, request_obj,img):
        if request_obj.get_shift_details_id() is  None:
            ShiftDetails_obj = ShiftDetails.objects.create(shift_date=request_obj.get_shift_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),scan_count=request_obj.get_scan_count(),supervisor=request_obj.get_supervisor(),remark=request_obj.get_remark(),supervisor_signature=img)
        else:
            ShiftDetails_obj = ShiftDetails.objects.filter(shift_details_id=request_obj.get_shift_details_id()).update(shift_date=request_obj.get_shift_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),scan_count=request_obj.get_scan_count(),supervisor=request_obj.get_supervisor(),remark=request_obj.get_remark(),updated_date=now(),supervisor_signature=img)
            ShiftDetails_obj = ShiftDetails.objects.get(shift_details_id=request_obj.get_shift_details_id())
        temp_response = ShiftDetail_response()
        temp_response.set_shift_details_id(ShiftDetails_obj.shift_details_id)
        temp_response.set_shift_date(str(ShiftDetails_obj.shift_date))
        temp_response.set_start_time(str(ShiftDetails_obj.start_time))
        temp_response.set_end_time(str(ShiftDetails_obj.end_time))
        temp_response.set_scan_count(ShiftDetails_obj.scan_count)
        temp_response.set_supervisor(ShiftDetails_obj.supervisor)
        temp_response.set_remark(ShiftDetails_obj.remark)
        temp_response.set_status(ShiftDetails_obj.status)
        return temp_response

    def fetch_shiftdetails(self, page_number, per_page, supervisor):

        # keywords = Product.objects.filter(
        #     name__icontains=name
        # )
        # keywords = Product.objects.filter(
        #     name__icontains=name
        # ).values('name','code','Category__name')
        condition = Q()
        if supervisor != None and supervisor != "":
            condition &= Q(supervisor=supervisor)
        keywords = ShiftDetails.objects.filter(condition).values('shift_details_id', 'shift_date', 'start_time', 'end_time','scan_count','supervisor','remark','status')
        count = ShiftDetails.objects.count()
        paginator = Paginator(keywords, per_page)
        data = []
        page_obj = paginator.get_page(page_number)
        for kw in page_obj.object_list:
            data.append({"shift_details_id": kw["shift_details_id"], "shift_date": kw["shift_date"], "start_time": kw["start_time"],"end_time":kw["end_time"],
                         "status": kw["status"],"scan_count":kw["scan_count"],"supervisor":kw["supervisor"],"remark":kw["remark"]})
        payload = {
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
                "count": count
            },
            "data": data
        }
        return JsonResponse(payload)

    def shiftdetails_get(self, shift_details_id):
        id_obj = ShiftDetails.objects.get(shift_details_id=shift_details_id)
        temp_response = ShiftDetail_response()
        temp_response.set_shift_details_id(id_obj.shift_details_id)
        temp_response.set_shift_date(str(id_obj.shift_date))
        temp_response.set_start_time(str(id_obj.start_time))
        temp_response.set_end_time(str(id_obj.end_time))
        temp_response.set_scan_count(id_obj.scan_count)
        temp_response.set_supervisor(id_obj.supervisor)
        temp_response.set_remark(id_obj.remark)
        temp_response.set_status(id_obj.status)
        return temp_response

    def modification_shiftdetails(self, shift_details_id, status):
        modification_obj = ShiftDetails.objects.filter(shift_details_id=shift_details_id).update(status=status)
        if modification_obj == 0:
            response = Error()
            response.set_code("ID NOT MATCHED")
            # response.set_name("Username already existed")
            return response
        else:
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj

class dropdown_service:

    def create_dropdown(self, request_obj):
        if request_obj.get_drop_down_id() is  None:
            DropDown_obj = DropDown.objects.create(list_item=request_obj.get_list_item(),list_type=request_obj.get_list_type())
        else:
            DropDown_obj = DropDown.objects.filter(drop_down_id=request_obj.get_drop_down_id()).update(list_item=request_obj.get_list_item(),list_type=request_obj.get_list_type())
            DropDown_obj = DropDown.objects.get(drop_down_id=request_obj.get_drop_down_id())
        temp_response = DropDown_response()
        temp_response.set_drop_down_id(DropDown_obj.drop_down_id)
        temp_response.set_list_item(DropDown_obj.list_item)
        temp_response.set_list_type(DropDown_obj.list_type)
        temp_response.set_status(DropDown_obj.status)
        return temp_response

    # def fetch_dropdown(self, vys_page, list_type,limit):
    #     try:
    #         condition = Q(status=1)
    #         if list_type != " " and list_type != None:
    #             condition &= Q(list_type=list_type)
    #         obj = DropDown.objects.filter(condition)[
    #               vys_page.get_offset():vys_page.get_query_limit()]
    #
    #         list_length = len(obj)
    #         pro_list = Demo_List()
    #         if list_length <= 0:
    #             return pro_list
    #         else:
    #
    #             for i in obj:
    #                 temp_response = DropDown_response()
    #                 temp_response.set_drop_down_id(i.drop_down_id)
    #                 temp_response.set_list_item(i.list_item)
    #                 temp_response.set_list_type(i.list_type)
    #                 temp_response.set_status(i.status)
    #
    #                 pro_list.append(temp_response)
    #             vpage = DemoPaginator(obj, vys_page.get_index(), str(limit))
    #             pro_list.set_pagination(vpage)
    #             return pro_list
    #     except Exception as e:
    #         error_obj = Error()
    #         print(e)
    #         # error_obj.set_code(ErrorMessage.INVALID_DATA)
    #         error_obj.set_description(str(e))
    #         return error_obj

    def dropdown_get(self, drop_down_id):
        id_obj = DropDown.objects.get(drop_down_id=drop_down_id)
        temp_response = DropDown_response()
        temp_response.set_drop_down_id(id_obj.drop_down_id)
        temp_response.set_list_item(id_obj.list_item)
        temp_response.set_list_type(id_obj.list_type)
        temp_response.set_status(id_obj.status)
        return temp_response

    def modification_dropdown(self, drop_down_id, status,Flag):
        if Flag=='DELETE':
            modification_obj = DropDown.objects.get(drop_down_id=drop_down_id).delete()
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj
        else:
            modification_obj = DropDown.objects.filter(drop_down_id=drop_down_id).update(status=status)
            if modification_obj == 0:
                response = Error()
                response.set_code("ID NOT MATCHED")
                # response.set_name("Username already existed")
                return response
            else:
                success_obj = Success()
                success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
                success_obj.set_status(SuccessStatus.SUCCESS)
                return success_obj

    def fetch_dropdown(self, page_number, per_page, list_type):

        condition=Q()
        if list_type!=None and list_type!="":
            condition&=Q(list_type=list_type)
        keywords = DropDown.objects.filter(condition).values('drop_down_id','list_item' ,'list_type','status')
        count=DropDown.objects.count()
        paginator = Paginator(keywords, per_page)
        data=[]
        page_obj = paginator.get_page(page_number)
        for kw in page_obj.object_list:
            data.append({"drop_down_id": kw["drop_down_id"],"list_item":kw["list_item"],"list_type":kw["list_type"],"status":kw["status"]})

        payload = {
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
                "count":count
            },
            "data": data
        }
        return JsonResponse(payload)

