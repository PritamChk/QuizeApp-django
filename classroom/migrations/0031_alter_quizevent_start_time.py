# Generated by Django 4.0.2 on 2022-02-15 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0030_alter_answerset_id_alter_quizevent_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizevent',
            name='start_time',
            field=models.TimeField(blank=True, db_index=True, default=datetime.time(12, 39, 20, 293953)),
        ),
    ]
