# Generated by Django 4.0.2 on 2022-02-14 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0024_alter_quizevent_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='belongs_to_quiz_set',
        ),
        migrations.AlterField(
            model_name='quizevent',
            name='start_time',
            field=models.TimeField(blank=True, db_index=True, default=datetime.time(0, 39, 5, 554048)),
        ),
    ]