import datetime

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

    def create_Controll(self, request_obj):
        if request_obj.get_control_sheet_id() is  None:
            Controll_obj = ControlSheet.objects.create(device_id=request_obj.get_device_id(),control_operator_id=request_obj.get_control_operator_id(),check_date=request_obj.get_check_date(),signature=request_obj.get_signature())
        else:
            Controll_obj = ControlSheet.objects.filter(control_sheet_id=request_obj.get_control_sheet_id()).update(device_id=request_obj.get_device_id(),control_operator_id=request_obj.get_control_operator_id(),check_date=request_obj.get_check_date(),signature=request_obj.get_signature())
            Controll_obj = ControlSheet.objects.get(control_sheet_id=request_obj.get_control_sheet_id())
        temp_response = ControlSheet_response()
        temp_response.set_device_id(Controll_obj.device_id)
        temp_response.set_control_operator_id(Controll_obj.control_operator.operator_id)
        temp_response.set_control_sheet_id(Controll_obj.control_sheet_id)
        temp_response.set_signature(Controll_obj.signature)
        check_date_datetime = datetime.datetime.strptime(Controll_obj.check_date, "%Y-%m-%d %H:%M:%S")
        time_str = check_date_datetime.strftime("%H:%M:%S")
        temp_response.check_time=str(time_str)
        temp_response.set_check_date(str(Controll_obj.check_date))
        return temp_response

    def fetch_Controll(self, page_number,per_page, control_operator_id,search,location,company,device_id,start_date,end_date,start_time,end_time):
        from django.db.models import Q

        condition = Q()

        if search is not None and search != "":
            # If search is provided, filter based on search across device_id or operator_id
            condition |= Q(device_id=search) | Q(control_operator_id=search)
        else:
            # Apply individual filters if provided
            if control_operator_id is not None and control_operator_id != "":
                condition &= Q(control_operator_id=int(control_operator_id))
            if location is not None and location != "":
                condition &= Q(device__location=location)
            if company is not None and company != "":
                condition &= Q(control_operator__company=company)
            if device_id is not None and device_id != "":
                condition &= Q(device_id=int(device_id))
            if start_date is not None and start_date != "" and end_date is not None and end_date != "":
                condition &= Q(check_date__range=[start_date, end_date])
            elif start_date is not None and start_date != "":
                condition &= Q(check_date=start_date)
            elif start_time != None and start_time != "":
                condition &= Q(start_time=start_time)
            elif end_time != None and end_time != "":
                condition &= Q(end_time=end_time)


        keywords = ControlSheet.objects.filter(condition).values('device_id', 'control_sheet_id', 'control_operator_id',
                                                                 'check_date', 'status','signature')

        count = ControlSheet.objects.count()
        paginator = Paginator(keywords, per_page)
        data = []
        page_obj = paginator.get_page(page_number)
        for kw in page_obj.object_list:
            check_date_datetime = datetime.datetime.strptime(str(kw["check_date"]),  "%Y-%m-%d %H:%M:%S%z")
            time_str = check_date_datetime.strftime("%H:%M:%S")

            data.append({"device_id": kw["device_id"], "control_sheet_id": kw["control_sheet_id"], "control_operator_id": kw["control_operator_id"],
                         "check_date": str(kw["check_date"]),"check_time":time_str,
                         "status": kw["status"],"signature": kw["signature"]})
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

    # def fetch_Controll(self, vys_page, control_operator_id):
    #     try:
    #         condition = Q(status=1)
    #         if control_operator_id != " " and control_operator_id != None:
    #             condition &= Q(control_operator_id=control_operator_id)
    #         obj = ControlSheet.objects.filter(condition)[
    #               vys_page.get_offset():vys_page.get_query_limit()]
    #
    #         list_length = len(obj)
    #         pro_list = Demo_List()
    #         if list_length <= 0:
    #             return pro_list
    #         else:
    #
    #             for i in obj:
    #                 temp_response = ControlSheet_response()
    #                 temp_response.set_device_id(i.device_id)
    #                 temp_response.set_control_operator_id(i.control_operator.operator_id)
    #                 temp_response.set_control_sheet_id(i.control_sheet_id)
    #                 temp_response.set_check_date(str(i.check_date))
    #                 pro_list.append(temp_response)
    #             vpage = DemoPaginator(obj, vys_page.get_index(), 10)
    #             pro_list.set_pagination(vpage)
    #             return pro_list
    #     except Exception as e:
    #         error_obj = Error()
    #         print(e)
    #         # error_obj.set_code(ErrorMessage.INVALID_DATA)
    #         error_obj.set_description(str(e))
    #         return error_obj

    def Controll_get(self, control_sheet_id):
        id_obj = ControlSheet.objects.get(control_sheet_id=control_sheet_id)
        temp_response = ControlSheet_response()
        check_date_datetime = datetime.datetime.strptime(str(id_obj.check_date), "%Y-%m-%d %H:%M:%S%z")
        time_str = check_date_datetime.strftime("%H:%M:%S")
        temp_response.set_device_id(id_obj.device_id)
        temp_response.check_time = str(time_str)
        temp_response.set_signature(id_obj.signature)
        temp_response.set_control_operator_id(id_obj.control_operator.operator_id)
        temp_response.set_control_sheet_id(id_obj.control_sheet_id)
        temp_response.set_check_date(str(id_obj.check_date))

        return temp_response

    def modification_Controll(self, status, control_sheet_id):
        modification_obj = ControlSheet.objects.filter(control_sheet_id=control_sheet_id).update(status=status)
        success_obj = Success()
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        success_obj.set_status(SuccessStatus.SUCCESS)
        return success_obj

class checkrule_service:

    def create_checkrule(self, request_obj):
        if request_obj.get_checkrule_id() is  None:
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

    def checkrule_get(self, checkrule_id):
        id_obj = CheckRule.objects.get(checkrule_id=checkrule_id)
        temp_response = CheckRule_response()
        temp_response.set_rule_choice(id_obj.rule_choice)
        temp_response.set_checkrule_id(id_obj.checkrule_id)
        temp_response.set_rule_id(id_obj.rule_id)
        temp_response.set_control_sheet_id(id_obj.control_sheet_id)
        temp_response.set_remark(id_obj.remark)
        return temp_response


    def controllsheet_get(self, control_sheet_id):
        filter_obj = CheckRule.objects.filter(control_sheet_id=control_sheet_id)
        list_obj=Demo_List()
        for id_obj in filter_obj:
            temp_response = CheckRule_response()

            temp_response.set_rule_choice(id_obj.rule_choice)
            temp_response.set_checkrule_id(id_obj.checkrule_id)
            temp_response.set_rule_id(id_obj.rule_id)
            temp_response.set_control_sheet_id(id_obj.control_sheet_id)
            temp_response.set_remark(id_obj.remark)
            list_obj.append(temp_response)

        return list_obj

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


    def bulk_checkrule(self, request_obj,control_sheet_id):
        Controll_obj=[]
        for i in request_obj:
            currention_obj = CheckRule(rule_id=i["rule_id"],control_sheet_id=control_sheet_id,
                                                    rule_choice=i["rule_choice"],
                                                    remark=i["remark"])
            Controll_obj.append(currention_obj)
        obj=CheckRule.objects.bulk_create(Controll_obj)


class scandetails_service:

    def create_scandetails(self, request_obj):
        # try:
        if request_obj.get_scan_details_id() is  None:
            obj_validation=self.validation_scan(request_obj.get_operator_id())

            if obj_validation==True:
                ScanDetails_obj = ScanDetails.objects.create(device_id=request_obj.get_device_id(),operator_id=request_obj.get_operator_id(),scan_date=request_obj.get_scan_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),shift_details_id=request_obj.get_shift_details_id(),operator_sign=request_obj.get_operator_sign())
                temp_response = ScanDetails_response()
                temp_response.set_scan_details_id(ScanDetails_obj.scan_details_id)
                temp_response.set_device_id(ScanDetails_obj.device_id)
                temp_response.set_operator_id(ScanDetails_obj.operator_id)
                temp_response.set_scan_date(str(ScanDetails_obj.scan_date))
                temp_response.set_start_time(ScanDetails_obj.start_time)
                temp_response.set_end_time(ScanDetails_obj.end_time)
                temp_response.operator_name = str(ScanDetails_obj.operator.first_name) + " " + str(
                    (ScanDetails_obj.operator.last_name))
                temp_response.operator_sign=ScanDetails_obj.operator_sign
                temp_response.created_date = str(ScanDetails_obj.created_date)
                temp_response.status_code = 200
                return temp_response
            else:
                error=Error()
                error.set_status(400)
                error.set_description("vaild break time")
                return error.to_response()
        else:
            ScanDetails_obj = ScanDetails.objects.filter(scan_details_id=request_obj.get_scan_details_id()).update(device_id=request_obj.get_device_id(),operator_id=request_obj.get_operator_id(),scan_date=request_obj.get_scan_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),shift_details_id=request_obj.get_shift_details_id(),updated_date=now(),operator_sign=request_obj.get_operator_sign())
            ScanDetails_obj = ScanDetails.objects.get(scan_details_id=request_obj.get_scan_details_id())
        temp_response = ScanDetails_response()
        temp_response.set_scan_details_id(ScanDetails_obj.scan_details_id)
        temp_response.set_device_id(ScanDetails_obj.device_id)
        temp_response.set_operator_id(ScanDetails_obj.operator_id)
        temp_response.set_scan_date(str(ScanDetails_obj.scan_date))
        temp_response.set_start_time(str(ScanDetails_obj.start_time))
        temp_response.set_end_time(str(ScanDetails_obj.end_time))
        temp_response.operator_name=str(ScanDetails_obj.operator.first_name)+" "+str((ScanDetails_obj.operator.last_name))
        temp_response.operator_sign = ScanDetails_obj.operator_sign
        temp_response.created_date = str(ScanDetails_obj.created_date)
        temp_response.status_code = 200
        return temp_response

    # def fetch_scandetails(self, vys_page, shift_details):
    #     try:
    #         condition = Q(status=1)
    #         if shift_details != " " and shift_details != None:
    #             condition &= Q(shift_details_id=shift_details)
    #         obj = ScanDetails.objects.filter(condition)[
    #               vys_page.get_offset():vys_page.get_query_limit()]
    #
    #         list_length = len(obj)
    #         pro_list = Demo_List()
    #         if list_length <= 0:
    #             return pro_list
    #         else:
    #
    #             for i in obj:
    #                 temp_response = ScanDetails_response()
    #                 temp_response.set_scan_details_id(i.scan_details_id)
    #                 temp_response.set_device_id(i.device_id)
    #                 temp_response.set_operator_id(i.operator_id)
    #                 temp_response.set_scan_date(str(i.scan_date))
    #                 temp_response.set_start_time(str(i.start_time))
    #                 temp_response.set_end_time(str(i.end_time))
    #                 temp_response.set_status(i.status)
    #
    #                 pro_list.append(temp_response)
    #             vpage = DemoPaginator(obj, vys_page.get_index(), 10)
    #             pro_list.set_pagination(vpage)
    #             return pro_list
    #     except Exception as e:
    #         error_obj = Error()
    #         print(e)
    #         # error_obj.set_code(ErrorMessage.INVALID_DATA)
    #         error_obj.set_description(str(e))
    #         return error_obj

    def fetch_ScanDetails(self, page_number, per_page, shift_details, query_text,company,device_id,operator_id,start_date,end_date,start_time,end_time,supervisor_name):
        from django.db.models import Q
        from django.core.paginator import Paginator
        from django.http import JsonResponse


        condition = Q()

        if query_text is not None and query_text != "":
            # If query_text is provided, filter based on query_text across device_id or operator_id
            condition |= Q(device_id=query_text) | Q(operator_id=query_text)
        else:
            # Apply individual filters if provided
            if company is not None and company != "":
                condition &= Q(operator__company__icontains=company)
            if device_id is not None and device_id != "":
                condition &= Q(device_id=int(device_id))
            if operator_id is not None and operator_id != "":
                condition &= Q(operator_id=int(operator_id))
            if shift_details is not None and shift_details != "":
                condition &= Q(shift_details_id=int(shift_details))
            if start_date is not None and start_date != "" and end_date is not None and end_date != "":
                condition &= Q(scan_date__range=[start_date, end_date])
            elif start_date is not None and start_date != "":
                condition &= Q(scan_date__gte=start_date)
            elif end_date is not None and end_date != "":
                condition &= Q(scan_date__lte=end_date)
            if start_time is not None and start_time != "":
                condition &= Q(start_time__gte=start_time)
            if end_time is not None and end_time != "":
                condition &= Q(end_time__lte=end_time)
            if supervisor_name is not None and supervisor_name != "":
                condition &= Q(shift_details__supervisor__icontains=supervisor_name)

        # Fetch the filtered results
        keywords = ScanDetails.objects.filter(condition).values(
            'scan_details_id', 'device_id', 'operator_id', 'scan_date', 'start_time', 'end_time',
            'shift_details', 'status', 'operator__first_name', 'operator__last_name', 'shift_details__supervisor',
            'created_date', 'operator_sign'
        ).order_by("-created_date")

        count = ScanDetails.objects.filter(condition).count()
        paginator = Paginator(keywords, per_page)
        data = []
        page_obj = paginator.get_page(page_number)

        for kw in page_obj.object_list:
            data.append({
                "scan_details_id": kw["scan_details_id"],
                "device_id": kw["device_id"],
                "operator_id": kw["operator_id"],
                "scan_date": str(kw["scan_date"]),
                "created_date": str(kw["created_date"]),
                "start_time": str(kw["start_time"]),
                "shift_details": kw["shift_details"],
                "end_time": str(kw["end_time"]),
                "operator_name": str(kw["operator__first_name"]) + " " + str(kw["operator__last_name"]),
                "status": kw["status"],
                "supervisor": kw["shift_details__supervisor"],
                "operator_sign": kw["operator_sign"]
            })

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


    def scandetails_get(self, scan_details_id):
        id_obj = ScanDetails.objects.get(scan_details_id=scan_details_id)
        temp_response = ScanDetails_response()
        temp_response.set_scan_details_id(id_obj.scan_details_id)
        temp_response.set_device_id(id_obj.device_id)
        temp_response.set_shift_details_id(id_obj.shift_details_id)
        temp_response.set_operator_id(id_obj.operator.operator_id)
        temp_response.operator_name = str(id_obj.operator.first_name)+" "+str(id_obj.operator.last_name)
        temp_response.set_scan_date(str(id_obj.scan_date))
        temp_response.set_start_time(str(id_obj.start_time))
        temp_response.set_end_time(str(id_obj.end_time))
        temp_response.set_status(id_obj.status)
        temp_response.operator_sign = id_obj.operator_sign
        temp_response.created_date = str(id_obj.created_date)

        return temp_response

    def modification_scandetails(self,scan_details_id, status,Flag):
        if Flag=='DELETE':
            modification_obj = ScanDetails.objects.get(scan_details_id=scan_details_id).delete()
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj
        else:

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
            Time_obj = TimeMaintenance.objects.filter(time_type="interval",current_status=True)
            # Assuming Time_obj has an attribute `desired_minutes` which specifies the allowed time frame in minutes
            allowed_minutes = Time_obj[0].decided_minutes

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

    def create_shiftdetails(self, request_obj):
        if request_obj.get_shift_details_id() is  None:
            ShiftDetails_obj = ShiftDetails.objects.create(shift_date=request_obj.get_shift_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),scan_count=request_obj.get_scan_count(),supervisor=request_obj.get_supervisor(),remark=request_obj.get_remark())
        else:
            ShiftDetails_obj = ShiftDetails.objects.filter(shift_details_id=request_obj.get_shift_details_id()).update(shift_date=request_obj.get_shift_date(),start_time=request_obj.get_start_time(),end_time=request_obj.get_end_time(),scan_count=request_obj.get_scan_count(),supervisor=request_obj.get_supervisor(),remark=request_obj.get_remark(),updated_date=now())
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

    def modification_shiftdetails(self, shift_details_id, status,Flag):
        if Flag=='DELETE':
            modification_obj = ShiftDetails.objects.get(shift_details_id=shift_details_id).delete()
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj
        else:

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

    def fetch_dropdown(self, page_number, per_page, list_type,search):
        from django.db.models import Q

        condition = Q()

        if search is not None and search != "":
            # If search is provided, filter based on search across multiple fields
            condition |= Q(list_item__icontains=search) | Q(list_type__icontains=search)
        else:
            # Apply individual filters if provided
            if list_type is not None and list_type != "":
                condition &= Q(list_type=list_type)

        # Fetch the filtered results
        keywords = DropDown.objects.filter(condition).values('drop_down_id', 'list_item', 'list_type', 'status')

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

