# Generated by Django 4.0.2 on 2022-02-14 16:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0019_alter_quizevent_start_time_alter_quizset_quiz_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizevent',
            name='start_time',
            field=models.TimeField(blank=True, db_index=True, default=datetime.time(21, 38, 39, 84684)),
        ),
        migrations.RemoveField(
            model_name='quizset',
            name='quiz_event',
        ),
        migrations.AddField(
            model_name='quizset',
            name='quiz_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizsets', to='classroom.quizevent'),
        ),
    ]
