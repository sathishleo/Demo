# Generated by Django 4.2.13 on 2024-07-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0012_controlsheet_check_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlsheet',
            name='check_date',
            field=models.CharField(max_length=40, null=True),
        ),
    ]