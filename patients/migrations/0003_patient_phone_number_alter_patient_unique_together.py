# Generated by Django 4.2.1 on 2023-06-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='4321', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together={('last_name', 'first_name', 'patronymic', 'date_of_birth')},
        ),
    ]
