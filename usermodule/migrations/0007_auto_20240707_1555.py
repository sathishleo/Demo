# Generated by Django 3.2.25 on 2024-07-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0006_scandetails_operator_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pausedetails',
            name='pause_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='pausedetails',
            name='play_time',
            field=models.TimeField(),
        ),
    ]
