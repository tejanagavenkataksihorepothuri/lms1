# Generated by Django 5.0.1 on 2025-02-19 09:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management', '0004_employee_last_leave_increment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_leave_increment',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
