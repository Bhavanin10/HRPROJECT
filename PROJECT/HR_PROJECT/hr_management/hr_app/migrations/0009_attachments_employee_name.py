# Generated by Django 3.0.4 on 2020-03-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0008_remove_attachments_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachments',
            name='EMPLOYEE_NAME',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
