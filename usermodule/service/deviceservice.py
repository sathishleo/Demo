from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.utils.timezone import now

from usermodule.data.response.deviceresponse import device_response, Operator_response, ECAC_response
from usermodule.models import Device, Operator, ECAC
from utlis.dataservice.demo_list import Demo_List
from utlis.dataservice.demo_paginator import DemoPaginator
from utlis.dataservice.error import Error
from utlis.dataservice.success import Success, SuccessMessage, SuccessStatus


class deviceservice:


    def create_device(self,request_obj):
        if  request_obj.get_device_id() is  None:
            device_obj=Device.objects.create(device_model=request_obj.get_device_model(),device_number=request_obj.get_device_number(),monitor_brand=request_obj.get_monitor_brand(),location=request_obj.get_location(),software_version=request_obj.get_software_version(),keyboard_brand=request_obj.get_keyboard_brand(),tunnel_size=request_obj.get_tunnel_size())
        else:
            device_obj=Device.objects.filter(device_id=request_obj.get_device_id()).update(device_model=request_obj.get_device_model(),tunnel_size=request_obj.get_tunnel_size(),device_number=request_obj.get_device_number(),monitor_brand=request_obj.get_monitor_brand(),location=request_obj.get_location(),software_version=request_obj.get_software_version(),keyboard_brand=request_obj.get_keyboard_brand(),updated_date=now())
            device_obj = Device.objects.get(device_id=request_obj.get_device_id())
        temp_response = device_response()
        temp_response.set_device_id(device_obj.device_id)
        temp_response.set_device_number(device_obj.device_number)
        temp_response.set_device_model(device_obj.device_model)
        temp_response.set_tunnel_size(device_obj.tunnel_size)
        temp_response.set_keyboard_brand(device_obj.keyboard_brand)
        temp_response.set_location(device_obj.location)
        temp_response.set_monitor_brand(device_obj.monitor_brand)
        temp_response.set_software_version(device_obj.software_version)
        temp_response.set_status(device_obj.status)
        return temp_response


    def device_get(self,device_id):
        id_obj=Device.objects.get(device_id=device_id)
        temp_response = device_response()
        temp_response.set_device_id(id_obj.device_id)
        temp_response.set_device_number(id_obj.device_number)
        temp_response.set_tunnel_size(id_obj.tunnel_size)
        temp_response.set_device_model(id_obj.device_model)
        temp_response.set_keyboard_brand(id_obj.keyboard_brand)
        temp_response.set_location(id_obj.location)
        temp_response.set_monitor_brand(id_obj.monitor_brand)
        temp_response.set_software_version(id_obj.software_version)
        temp_response.set_status(id_obj.status)
        return temp_response

    def fetch_device(self,  page_number, per_page, device_model,query_text):
        if query_text == None and query_text == "":
            keywords = Device.objects.filter(
                Q(device_model__icontains=query_text) |
                Q(device_number__icontains=query_text) |
                Q(monitor_brand__icontains=query_text)).values('device_id', 'device_model', 'device_number', 'tunnel_size', 'status',
                     'monitor_brand', 'location', 'software_version', 'keyboard_brand')
        else:
            condition = Q()
            if device_model != None and device_model != "":
                condition &= Q(device_model__icontains=device_model)
            keywords = Device.objects.filter(condition).values('device_id', 'device_model', 'device_number',
                                                               'tunnel_size', 'status',
                                                                              'monitor_brand', 'location',
                                                               'software_version', 'keyboard_brand')

        count = Device.objects.count()
        paginator = Paginator(keywords, per_page)
        data = []
        page_obj = paginator.get_page(page_number)
        for kw in page_obj.object_list:
            data.append({"device_id": kw["device_id"], "device_model": kw["device_model"], "device_number": kw["device_number"],
                         "tunnel_size": kw["tunnel_size"],
                         "status": kw["status"], "monitor_brand": kw["monitor_brand"], "location": kw["location"],
                         "keyboard_brand": kw["keyboard_brand"]  ,"software_version": kw["software_version"]})
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

    def modification_device(self,device_id,status,Flag):
        if Flag =="DELETE":
            modification_obj = Device.objects.get(device_id=device_id).delete()
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj
        else:

            modification_obj=Device.objects.filter(device_id=int(device_id)).update(status=status)
            if modification_obj==0:
                response = Error()
                response.set_code("ID NOT MATCHED")
                response.set_name("Username already existed")
                return response
            else:
                success_obj=Success()
                success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
                success_obj.set_status(SuccessStatus.SUCCESS)
                return success_obj


class Operator_service:

    def create_operator(self, request_obj):
        if request_obj.get_operator_id() is  None:
            operator_obj = Operator.objects.create(first_name=request_obj.get_first_name(),last_name=request_obj.get_last_name(),company=request_obj.get_company(),employee_id=request_obj.get_employee_id(),email_address=request_obj.get_email_address(),phone=request_obj.get_phone())
        else:
            operator_obj = Operator.objects.filter(operator_id=request_obj.get_operator_id()).update(first_name=request_obj.get_first_name(),last_name=request_obj.get_last_name(),company=request_obj.get_company(),employee_id=request_obj.get_employee_id(),email_address=request_obj.get_email_address(),phone=request_obj.get_phone(),updated_date=now())
            operator_obj = Operator.objects.get(operator_id=request_obj.get_operator_id())
        temp_response = Operator_response()
        temp_response.set_operator_id(operator_obj.operator_id)
        temp_response.set_first_name(operator_obj.first_name)
        temp_response.set_last_name(operator_obj.last_name)
        temp_response.set_company(operator_obj.company)
        temp_response.set_employee_id(operator_obj.employee_id)
        temp_response.set_email_address(operator_obj.email_address)
        temp_response.set_phone(operator_obj.phone)
        return temp_response

    def fetch_operator(self, page_number, per_page, first_name,query_text):

        if query_text==None and query_text=="" :
            keywords = Operator.objects.filter(
                Q(first_name__icontains=query_text) |
                Q(last_name__icontains=query_text) |
                Q(company__icontains=query_text)
            ).values('operator_id', 'first_name', 'last_name', 'company', 'employee_id', 'email_address', 'phone',
                     'status')
        else:

            condition = Q()
            if first_name != None and first_name != "":
                condition &= Q(first_name__icontains=first_name)
            keywords = Operator.objects.filter(condition).values('operator_id', 'first_name', 'last_name', 'company',
                                                                 'employee_id', 'email_address', 'phone', 'status')
        count = Operator.objects.count()
        paginator = Paginator(keywords, per_page)
        data = []
        page_obj = paginator.get_page(page_number)
        for kw in page_obj.object_list:
            data.append({"operator_id": kw["operator_id"], "first_name": kw["first_name"], "last_name": kw["last_name"],"company":kw["company"],
                         "status": kw["status"],"employee_id":kw["employee_id"],"email_address":kw["email_address"],"phone":kw["phone"]})
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

    def operator_get(self, operator_id):
        id_obj = Operator.objects.get(operator_id=operator_id)
        temp_response = Operator_response()
        temp_response.set_operator_id(id_obj.operator_id)
        temp_response.set_first_name(id_obj.first_name)
        temp_response.set_last_name(id_obj.last_name)
        temp_response.set_company(id_obj.company)
        temp_response.set_employee_id(id_obj.employee_id)
        temp_response.set_email_address(id_obj.email_address)
        temp_response.set_phone(id_obj.phone)
        return temp_response

    def modification_operator(self,operator_id,status,Flag):
        if Flag=="DELETE":
            modification_obj = Operator.objects.get(operator_id=operator_id).delete()
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj
        else:
            modification_obj = Operator.objects.filter(operator_id=operator_id).update(status=status)
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

class ECAC_service:

    def create_ecac(self, request_obj):
        if request_obj.get_ecac_id() is  None:
            ecac_obj = ECAC.objects.create(test_view=request_obj.get_test_view(),test_date=request_obj.get_test_date(),test_time=request_obj.get_test_time(),device_id=request_obj.get_device_id(),operator_id=request_obj.get_operator_id(),position=request_obj.get_position(),test_1test_2=request_obj.get_test1_test2(),test_3=request_obj.get_test3(),test_4a=request_obj.get_test4a(),test_4b=request_obj.get_test4b(),test_5=request_obj.get_test5())
        else:
            ecac_obj = ECAC.objects.filter(ecac_id=request_obj.get_ecac_id()).update(test_view=request_obj.get_test_view(),test_date=request_obj.get_test_date(),test_time=request_obj.get_test_time(),device_id=request_obj.get_device_id(),operator_id=request_obj.get_operator_id(),position=request_obj.get_position(),test_1test_2=request_obj.get_test1_test2(),test_3=request_obj.get_test3(),test_4a=request_obj.get_test4a(),test_4b=request_obj.get_test4b(),test_5=request_obj.get_test5(),updated_date=now())
            ecac_obj = ECAC.objects.get(ecac_id=request_obj.get_ecac_id())
        temp_response = ECAC_response()
        temp_response.set_operator_id(ecac_obj.operator_id)
        temp_response.set_device_id(ecac_obj.device_id)
        temp_response.set_ecac_id(ecac_obj.ecac_id)
        temp_response.set_position(ecac_obj.position)
        temp_response.set_test_date(str(ecac_obj.test_date))
        temp_response.set_test_time(str(ecac_obj.test_time))
        temp_response.set_test_view(ecac_obj.test_view)
        temp_response.set_test1_test2(ecac_obj.test_1test_2)
        temp_response.set_test3(ecac_obj.test_3)
        temp_response.set_test4a(ecac_obj.test_4a)
        temp_response.set_test4b(ecac_obj.test_4b)
        temp_response.set_test_5(ecac_obj.test_5)
        return temp_response

    def fetch_ecac(self, page_number, per_page, test_view,query_text,start_date,end_date,start_time,end_time,device_id,tunnel_size,device_model,software_version,operator_id,location,company,position):
        if query_text==None and query_text=="" :
            keywords = ECAC.objects.filter(
                Q(test_view__icontains=query_text) |
                Q(device_id__icontains=query_text) |
                Q(operator_id__icontains=query_text)
            ).values('operator_id', 'first_name', 'last_name', 'company', 'employee_id', 'email_address', 'phone',
                     'status')
        else:
            condition = Q()
            if test_view != None and test_view != "":
                condition &= Q(test_view__icontains=test_view)
            if start_date != None and start_date != "":
                condition &= Q(test_date__icontains=start_date)
            if end_date != None and end_date != "":
                condition &= Q(test_date__icontains=end_date)
            if start_time != None and start_time != "":
                condition &= Q(test_time__icontains=start_time)
            if end_time != None and end_time != "":
                condition &= Q(test_view__icontains=end_time)
            if device_id != None and device_id != "":
                condition &= Q(device_id=device_id)
            if tunnel_size != None and tunnel_size != "":
                condition &= Q(device__tunnel_size=tunnel_size)
            if device_model != None and device_model != "":
                condition &= Q(device__device_model=device_model)
            if software_version != None and software_version != "":
                condition &= Q(device__software_version=software_version)
            if operator_id != None and operator_id != "":
                condition &= Q(operator_id=operator_id)
            if location != None and location != "":
                condition &= Q(device__location=location)
            if company != None and company != "":
                condition &= Q(operator__company=company)
            if position != None and position != "":
                condition &= Q(position=position)
            if start_time != None and start_time != "" and end_time != None and end_time != "":
                condition &= Q(test_time__range=[start_time,end_time])
            if start_date != None and start_date != "" and end_date != None and end_date != "":
                condition &= Q(test_date__range=[start_date,end_date])
            keywords = ECAC.objects.filter(condition).values('operator_id', 'device_id', 'ecac_id', 'position',
                                                                 'test_date', 'test_time', 'test_view', 'status','test_1test_2','test_3','test_4a','test_4b','test_5')
            count = ECAC.objects.count()
            paginator = Paginator(keywords, per_page)
            data = []
            page_obj = paginator.get_page(page_number)
            for kw in page_obj.object_list:
                data.append({"operator_id": kw["operator_id"], "device_id": kw["device_id"], "ecac_id": kw["ecac_id"],
                             "position": kw["position"],
                             "test_date": kw["test_date"], "test_time": kw["test_time"], "test_view": kw["test_view"],
                             "status": kw["status"],"test_1test_2": kw["test_1test_2"],"test_3": kw["test_3"],"test_4a": kw["test_4a"],"test_4b": kw["test_4b"],"test_5": kw["test_5"]})
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

    def ecac_get(self, ecac_id):
        id_obj = ECAC.objects.get(ecac_id=ecac_id)
        temp_response = ECAC_response()
        temp_response.set_operator_id(id_obj.operator_id)
        temp_response.set_device_id(id_obj.device_id)
        temp_response.set_ecac_id(id_obj.ecac_id)
        temp_response.set_position(id_obj.position)
        temp_response.set_test_date(str(id_obj.test_date))
        temp_response.set_test_time(str(id_obj.test_time))
        temp_response.set_test_view(id_obj.test_view)
        temp_response.set_test1_test2(id_obj.test_1test_2)
        temp_response.set_test3(id_obj.test_3)
        temp_response.set_test4a(id_obj.test_4a)
        temp_response.set_test4b(id_obj.test_4b)
        temp_response.set_test_5(id_obj.test_5)
        return temp_response
    def modification_ecac(self, ecac_id,status,Flag):
        if Flag=='DELETE':
            modification_obj = ECAC.objects.get(ecac_id=ecac_id).delete()
            success_obj = Success()
            success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
            success_obj.set_status(SuccessStatus.SUCCESS)
            return success_obj
        else:
            modification_obj = ECAC.objects.filter(ecac_id=ecac_id).update(status=status)

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


