# Generated by Django 3.0.4 on 2020-03-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0010_auto_20200319_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='PANNumber',
            field=models.CharField(max_length=10),
        ),
    ]
