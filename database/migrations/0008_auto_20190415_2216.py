# Generated by Django 2.1.3 on 2019-04-15 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20190415_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='current_zone',
        ),
        migrations.AddField(
            model_name='device',
            name='current_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.Danger_zone'),
        ),
    ]
