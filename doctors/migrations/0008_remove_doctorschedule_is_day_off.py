# Generated by Django 4.2.1 on 2023-09-03 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_doctorschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorschedule',
            name='is_day_off',
        ),
    ]
