# Generated by Django 4.2.1 on 2023-09-04 08:55

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_remove_patientprofile_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2023, 9, 4))]),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
