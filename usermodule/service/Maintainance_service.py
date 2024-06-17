from django.db.models import Q
from django.utils.timezone import now

from usermodule.data.response.scanresponse import ScanDetails_response, ShiftDetail_response, DropDown_response, \
    TimeMaintenance_response, PauseDetails_response
from usermodule.models import TimeMaintenance, PauseDetails
from utlis.dataservice.demo_list import Demo_List
from utlis.dataservice.demo_paginator import DemoPaginator
from utlis.dataservice.error import Error
from utlis.dataservice.success import Success, SuccessMessage, SuccessStatus


class TimeMaintenance_service:

    def create_shiftmaintance(self, request_obj):
        if request_obj.get_time_maintenance_id() is  None:
            TimeMaintenance_obj = TimeMaintenance.objects.create(time_type=request_obj.get_time_type(),change_date=request_obj.get_change_date(),decided_minutes=request_obj.get_decided_minutes())
        else:
            TimeMaintenance_obj = TimeMaintenance.objects.filter(time_maintenance_id=request_obj.get_id()).update(time_type=request_obj.get_time_type(),change_date=request_obj.get_change_date(),decided_minutes=request_obj.get_decided_minutes(),updated_date=now())
            TimeMaintenance_obj = TimeMaintenance.objects.filter(time_maintenance_id=request_obj.get_id())
        temp_response = TimeMaintenance_response()
        temp_response.set_time_maintenance_id(TimeMaintenance_obj.time_maintenance_id)
        temp_response.set_time_type(TimeMaintenance_obj.time_type)
        temp_response.set_change_date(str(TimeMaintenance_obj.change_date))
        temp_response.set_decided_minutes(TimeMaintenance_obj.decided_minutes)
        temp_response.set_current_status(TimeMaintenance_obj.current_status)
        temp_response.set_status(TimeMaintenance_obj.status)
        return temp_response

    def fetch_shiftmaintainance(self, vys_page, time_type):
        try:
            condition = Q(status=1)
            if time_type != " " and time_type != None:
                condition &= Q(time_type=time_type)
            obj = TimeMaintenance.objects.filter(condition)[
                  vys_page.get_offset():vys_page.get_query_limit()]

            list_length = len(obj)
            pro_list = Demo_List()
            if list_length <= 0:
                return pro_list
            else:

                for i in obj:
                    temp_response = TimeMaintenance_response()
                    temp_response.set_time_maintenance_id(i.time_maintenance_id)
                    temp_response.set_time_type(i.time_type)
                    temp_response.set_change_date(str(i.change_date))
                    temp_response.set_decided_minutes(i.decided_minutes)
                    temp_response.set_current_status(i.current_status)
                    temp_response.set_status(i.status)
                    pro_list.append(temp_response)
                vpage = DemoPaginator(obj, vys_page.get_index(), 5)
                pro_list.set_pagination(vpage)
                return pro_list
        except Exception as e:
            error_obj = Error()
            print(e)
            # error_obj.set_code(ErrorMessage.INVALID_DATA)
            error_obj.set_description(str(e))
            return error_obj

    def shiftmaintainance_get(self, time_maintenance_id):
        id_obj = TimeMaintenance.objects.get(time_maintenance_id=time_maintenance_id)
        temp_response = TimeMaintenance_response()
        temp_response.set_time_maintenance_id(id_obj.time_maintenance_id)
        temp_response.set_time_type(id_obj.time_type)
        temp_response.set_change_date(str(id_obj.change_date))
        temp_response.set_decided_minutes(id_obj.decided_minutes)
        temp_response.set_current_status(id_obj.current_status)
        temp_response.set_status(id_obj.status)
        return temp_response

    def modification_shiftmaintainance(self, time_maintenance_id, status):
        modification_obj = TimeMaintenance.objects.filter(time_maintenance_id=time_maintenance_id).update(status=status)
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


class PauseDetails_service:

    def create_scanmaintance(self, request_obj):
        if request_obj.get_id() is  None:
            PauseDetails_obj = PauseDetails.objects.create(scan_details_id=request_obj.get_scan_details_id(),pause_time=request_obj.get_pause_time(),play_time=request_obj.get_play_time(),remarks=request_obj.get_remarks())
        else:
            PauseDetails_obj = PauseDetails.objects.filter(pause_details_id=request_obj.get_pause_details_id()).update(scan_details_id=request_obj.get_scan_details_id(),pause_time=request_obj.get_pause_time(),play_time=request_obj.get_play_time(),remarks=request_obj.get_remarks(),updated_date=now())
            PauseDetails_obj = PauseDetails.objects.filter(pause_details_id=request_obj.get_pause_details_id())
        temp_response = PauseDetails_response()
        temp_response.set_pause_details_id(PauseDetails_obj.pause_details_id)
        temp_response.set_scan_details_id(PauseDetails_obj.scan_details_id)
        temp_response.set_play_time(str(PauseDetails_obj.play_time))
        temp_response.set_pause_time(str(PauseDetails_obj.pause_time))
        temp_response.set_remarks(PauseDetails_obj.remarks)
        temp_response.set_status(PauseDetails_obj.status)
        return temp_response

    def fetch_scanmaintainance(self, vys_page, scan_details_id):
        try:
            condition = Q(status=1)
            if scan_details_id != " " and scan_details_id != None:
                condition &= Q(scan_details_id=scan_details_id)
            obj = PauseDetails.objects.filter(condition)[
                  vys_page.get_offset():vys_page.get_query_limit()]

            list_length = len(obj)
            pro_list = Demo_List()
            if list_length <= 0:
                return pro_list
            else:

                for i in obj:
                    temp_response = PauseDetails_response()
                    temp_response.set_pause_details_id(i.pause_details_id)
                    temp_response.set_scan_details_id(i.scan_details_id)
                    temp_response.set_play_time(str(i.play_time))
                    temp_response.set_pause_time(str(i.pause_time))
                    temp_response.set_remarks(i.remarks)
                    temp_response.set_status(i.status)
                    pro_list.append(temp_response)
                vpage = DemoPaginator(obj, vys_page.get_index(), 5)
                pro_list.set_pagination(vpage)
                return pro_list
        except Exception as e:
            error_obj = Error()
            print(e)
            # error_obj.set_code(ErrorMessage.INVALID_DATA)
            error_obj.set_description(str(e))
            return error_obj

    def scanmaintainance_get(self, id):
        id_obj = PauseDetails.objects.get(id=id)
        temp_response = PauseDetails_response()
        temp_response.set_pause_details_id(id_obj.pause_details_id)
        temp_response.set_scan_details_id(id_obj.scan_details_id)
        temp_response.set_play_time(str(id_obj.play_time))
        temp_response.set_pause_time(str(id_obj.pause_time))
        temp_response.set_remarks(id_obj.remarks)
        temp_response.set_status(id_obj.status)
        return temp_response

    def modification_scanmaintainance(self, status, id):
        modification_obj = PauseDetails.objects.filter(id=id).update(status=status)
        success_obj = Success()
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        success_obj.set_status(SuccessStatus.SUCCESS)
        return success_obj

