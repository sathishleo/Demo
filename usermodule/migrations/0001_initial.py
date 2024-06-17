# Generated by Django 3.2.25 on 2024-06-14 11:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_model', models.CharField(max_length=60, null=True)),
                ('device_number', models.CharField(max_length=40, null=True)),
                ('tunnel_size', models.CharField(max_length=75, null=True)),
                ('monitor_brand', models.CharField(max_length=60, null=True)),
                ('location', models.CharField(max_length=75, null=True)),
                ('software_version', models.CharField(max_length=75, null=True)),
                ('keyboard_brand', models.CharField(max_length=60, null=True)),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DropDown',
            fields=[
                ('drop_down_id', models.AutoField(primary_key=True, serialize=False)),
                ('list_item', models.CharField(max_length=150, null=True)),
                ('list_type', models.CharField(max_length=60, null=True)),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('operator_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('last_name', models.CharField(max_length=120, null=True)),
                ('company', models.CharField(max_length=75, null=True)),
                ('employee_id', models.CharField(max_length=40, null=True)),
                ('email_address', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('operator_img', models.ImageField(upload_to='operator_images/')),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftDetails',
            fields=[
                ('shift_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('scan_count', models.IntegerField(null=True)),
                ('supervisor', models.CharField(max_length=75, null=True)),
                ('supervisor_signature', models.ImageField(upload_to='supervisor_sign/')),
                ('remark', models.CharField(max_length=120, null=True)),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeMaintenance',
            fields=[
                ('time_maintenance_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_type', models.TextField(null=True)),
                ('decided_minutes', models.IntegerField(null=True)),
                ('change_date', models.DateField(null=True)),
                ('current_status', models.BooleanField(default=True)),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScanDetails',
            fields=[
                ('scan_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('scan_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('operator_signature', models.ImageField(upload_to='operator_signature/')),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.device')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.operator')),
                ('shift_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.shiftdetails')),
            ],
        ),
        migrations.CreateModel(
            name='PauseDetails',
            fields=[
                ('pause_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('pause_time', models.DateTimeField()),
                ('play_time', models.DateTimeField()),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('scan_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.scandetails')),
            ],
        ),
        migrations.CreateModel(
            name='ECAC',
            fields=[
                ('ecac_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_view', models.CharField(max_length=40, null=True)),
                ('test_date', models.DateField(null=True)),
                ('test_time', models.TimeField(null=True)),
                ('position', models.CharField(max_length=20, null=True)),
                ('test_1test_2', models.IntegerField(null=True)),
                ('test_3', models.IntegerField(null=True)),
                ('test_4a', models.IntegerField(null=True)),
                ('test_4b', models.IntegerField(null=True)),
                ('test_5', models.IntegerField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.device')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.operator')),
            ],
        ),
        migrations.CreateModel(
            name='ControlSheet',
            fields=[
                ('control_sheet_id', models.AutoField(primary_key=True, serialize=False)),
                ('check_date', models.DateField()),
                ('signature', models.ImageField(upload_to='controll_sheet_sign/')),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField()),
                ('updated_date', models.DateTimeField()),
                ('control_operator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.operator')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.device')),
            ],
        ),
        migrations.CreateModel(
            name='CheckRule',
            fields=[
                ('checkrule_id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_id', models.CharField(max_length=120)),
                ('rule_choice', models.IntegerField(null=True)),
                ('remark', models.CharField(max_length=150)),
                ('status', models.IntegerField(default=1)),
                ('created_by', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('control_sheet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usermodule.controlsheet')),
            ],
        ),
    ]
