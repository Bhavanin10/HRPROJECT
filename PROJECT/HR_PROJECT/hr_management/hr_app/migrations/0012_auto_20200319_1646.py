# Generated by Django 3.0.4 on 2020-03-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0011_auto_20200319_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='AdharNumber',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='UANNumber',
            field=models.IntegerField(default=None),
        ),
    ]
