# Generated by Django 3.0.4 on 2020-03-20 02:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0006_auto_20200319_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachments',
            name='EMPLOYEE_NAME',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='attachments',
            name='PASSPORT_SIZE_PHOTO',
            field=models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'img', 'png'], message='please choose the valid file')]),
        ),
    ]
