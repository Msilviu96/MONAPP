# Generated by Django 2.1.3 on 2019-06-03 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_auto_20190603_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 23, 2, 57, 313651)),
        ),
    ]
