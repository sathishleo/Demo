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

    def fetch_device(self,vys_page, device_model):
        try:
            condition=Q(status=1)
            if device_model!=" " and device_model!=None:
                condition&=Q(device_model=device_model)
            obj = Device.objects.filter(condition)[
                 vys_page.get_offset():vys_page.get_query_limit()]

            list_length = len(obj)
            pro_list = Demo_List()
            if list_length <= 0:
                return pro_list
            else:

                for i in obj:
                    temp_response = device_response()
                    temp_response.set_device_id(i.device_id)
                    temp_response.set_device_number(i.device_number)
                    temp_response.set_tunnel_size(i.tunnel_size)
                    temp_response.set_device_model(i.device_model)
                    temp_response.set_keyboard_brand(i.keyboard_brand)
                    temp_response.set_location(i.location)
                    temp_response.set_monitor_brand(i.monitor_brand)
                    temp_response.set_software_version(i.software_version)
                    temp_response.set_status(i.status)
                    pro_list.append(temp_response)
                vpage = DemoPaginator(obj, vys_page.get_index(), 10)
                pro_list.set_pagination(vpage)
                return pro_list
        except Exception as e:
            error_obj = Error()
            print(e)
            error_obj.set_description(str(e))
            return error_obj
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

    def device_list(self, query_text):
        demo_list = Demo_List()  # Initialize the Demo_List instance
        data = Device.objects.filter(
            Q(device_model__icontains=query_text) |
            Q(device_number__icontains=query_text) |
            Q(monitor_brand__icontains=query_text) |
            Q(keyboard_brand__icontains=query_text)
        )

        if len(data) == 0:  # Check if no records are found
            response = Error()
            response.set_code("No Records in Operator")  # Set error code
            response.set_name("already existed")  # Set error message
            return response
        else:
            for id_obj in data:  # Iterate through the filtered device records
                temp_response = device_response()  # Create a new device_response instance
                # Set the fields of temp_response using the device record
                temp_response.set_device_id(id_obj.device_id)
                temp_response.set_device_number(id_obj.device_number)
                temp_response.set_tunnel_size(id_obj.tunnel_size)
                temp_response.set_device_model(id_obj.device_model)
                temp_response.set_keyboard_brand(id_obj.keyboard_brand)
                temp_response.set_location(id_obj.location)
                temp_response.set_monitor_brand(id_obj.monitor_brand)
                temp_response.set_software_version(id_obj.software_version)
                temp_response.set_status(id_obj.status)
                demo_list.append(temp_response)  # Append the response to the list
            return demo_list  # Return the list of device responses


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

    def fetch_operator(self, page_number, per_page, first_name):
        condition = Q()
        if first_name != None and first_name != "":
            condition &= Q(first_name__icontains=first_name)
        keywords = Operator.objects.filter(condition).values('operator_id', 'first_name', 'last_name', 'company','employee_id','email_address','phone','status')
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
        if Flag==True:
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


    def operator_list(self,query_text):
        demo_list = Demo_List()  # Initialize the Demo_List instance
        data = Device.objects.filter(
            Q(device_model__icontains=query_text) |
            Q(device_number__icontains=query_text) |
            Q(monitor_brand__icontains=query_text) |
            Q(keyboard_brand__icontains=query_text)
        )

        if len(data) == 0:  # Check if no records are found
            response = Error()
            response.set_code("No Records in Operator")  # Set error code
            response.set_name("already existed")  # Set error message
            return response
        else:  # Create an instance of Demo_List
            for operator in data:  # Iterate through each operator record
                temp_response = Operator_response()  # Create a new Operator_response instance
                # Set the fields of temp_response using the operator record
                temp_response.set_operator_id(operator.operator_id)
                temp_response.set_first_name(operator.first_name)
                temp_response.set_last_name(operator.last_name)
                temp_response.set_company(operator.company)
                temp_response.set_employee_id(operator.employee_id)
                temp_response.set_email_address(operator.email_address)
                temp_response.set_phone(operator.phone)
                demo_list.append(temp_response)  # Append the response to the list
            return demo_list  # Return the list of operator responses


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

    def fetch_ecac(self, page_number, per_page, test_view):
        condition = Q()
        if test_view != None and test_view != "":
            condition &= Q(test_view__icontains=test_view)
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
    def modification_ecac(self, ecac_id,status):
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


