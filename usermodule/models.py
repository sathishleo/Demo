
from django.db import models
import uuid

from django.utils.timezone import now
# from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
# gd_storage = GoogleDriveStorage()
# from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

# permission =  GoogleDriveFilePermission(
#    GoogleDrivePermissionRole.READER,
#    GoogleDrivePermissionType.USER,
#    "foo@mailinator.com"
# )
#
# gd_storage = GoogleDriveStorage(permissions=(permission, ))


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_model = models.CharField(max_length=60,null=True)
    device_number = models.CharField(max_length=40,null=True)
    tunnel_size = models.CharField(max_length=75,null=True)
    monitor_brand = models.CharField(max_length=60,null=True)
    location = models.CharField(max_length=75,null=True)
    software_version = models.CharField(max_length=75,null=True)
    keyboard_brand = models.CharField(max_length=60,null=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class Operator(models.Model):
    operator_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120,null=True)
    last_name = models.CharField(max_length=120,null=True)
    company = models.CharField(max_length=75,null=True)
    employee_id = models.CharField(max_length=40,null=True)
    email_address = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=20,null=True)
    operator_img = models.ImageField(upload_to='operator_images/')
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class ECAC(models.Model):
    ecac_id = models.AutoField(primary_key=True)
    test_view = models.CharField(max_length=40,null=True)
    test_date = models.DateField(null=True)
    test_time = models.TimeField(null=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    operator = models.ForeignKey(Operator, on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=20,null=True)
    test_1test_2 = models.IntegerField(null=True)
    test_3 = models.IntegerField(null=True)
    test_4a = models.IntegerField(null=True)
    test_4b = models.IntegerField(null=True)
    test_5 = models.IntegerField(null=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class ControlSheet(models.Model):
    control_sheet_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    control_operator = models.ForeignKey(Operator, on_delete=models.DO_NOTHING)
    check_date = models.DateTimeField()
    signature = models.ImageField(upload_to='controll_sheet_sign/')
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class CheckRule(models.Model):
    checkrule_id=models.AutoField(primary_key=True)
    control_sheet = models.ForeignKey(ControlSheet, on_delete=models.DO_NOTHING)
    rule_id = models.CharField(max_length=120)
    rule_choice = models.IntegerField(null=True)
    remark = models.CharField(max_length=150)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class ShiftDetails(models.Model):
    shift_details_id = models.AutoField(primary_key=True)
    shift_date = models.DateField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    scan_count = models.IntegerField(null=True)
    supervisor = models.CharField(max_length=75,null=True)
    supervisor_signature = models.ImageField(upload_to='supervisor_sign/')
    remark = models.CharField(max_length=120,null=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)


class ScanDetails(models.Model):
    scan_details_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    operator = models.ForeignKey(Operator, on_delete=models.DO_NOTHING)
    scan_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    operator_signature =  models.ImageField(upload_to='operator_signature/')
    operator_sign =  models.TextField(null=True)
    shift_details = models.ForeignKey(ShiftDetails, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class PauseDetails(models.Model):
    pause_details_id = models.AutoField(primary_key=True)
    scan_details_id = models.ForeignKey(ScanDetails, on_delete=models.CASCADE)
    pause_time = models.DateTimeField()
    play_time = models.DateTimeField()
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)


class DropDown(models.Model):
    drop_down_id=models.AutoField(primary_key=True)
    list_item = models.CharField(max_length=150,null=True)
    list_type = models.CharField(max_length=60,null=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)

class TimeMaintenance(models.Model):
    time_maintenance_id=models.AutoField(primary_key=True)
    time_type = models.TextField(null=True)
    decided_minutes = models.IntegerField(null=True)
    change_date = models.DateField(default=now)
    current_status=models.BooleanField(default=True)
    status = models.IntegerField(default=1)
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)
