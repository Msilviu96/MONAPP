# Generated by Django 2.1.3 on 2019-04-15 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_child_current_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='current_zone',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='database.Danger_zone'),
        ),
    ]