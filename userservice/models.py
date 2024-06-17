from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Module(models.Model):
    refid = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=64)
    logo = models.CharField(max_length=64, null=True, blank=True)
    url = models.CharField(max_length=128, null=True, blank=True)
    issys = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    module_order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'userservice_module'


class UserModuleMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'userservice_usermodulemapping'


class Role(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=64)
    issys = models.BooleanField(default=False)
    operation_name = models.CharField(max_length=64)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'userservice_role'


class RoleModule(models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'userservice_rolemodule'
class Employee(models.Model):
    full_name=models.CharField(max_length=245,null=True)
    email=models.EmailField(null=True)
    code=models.CharField(max_length=245,null=True)
    status=models.IntegerField(default=1)
    phone_no = models.IntegerField(blank=False,null=True)
    created_by=models.IntegerField(null=True)
    rm=models.BooleanField(default=False)
    counter = models.IntegerField(default=0, blank=False)
    user_id=models.IntegerField(null=True)
    created_date=models.DateTimeField(default=now)
    updated_by=models.IntegerField(null=True)
    updated_date=models.DateTimeField(default=now)


class RoleEmployee(models.Model):
    role = models.ForeignKey(RoleModule, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'userservice_roleemployee'
