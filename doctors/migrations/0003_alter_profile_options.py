# Generated by Django 4.2.1 on 2023-06-03 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_profile_options_profile_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_edit_profile', 'Can edit profile123')]},
        ),
    ]