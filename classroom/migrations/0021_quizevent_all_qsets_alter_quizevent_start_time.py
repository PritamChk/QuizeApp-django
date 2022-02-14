# Generated by Django 4.0.2 on 2022-02-14 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0020_alter_quizevent_start_time_remove_quizset_quiz_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizevent',
            name='all_qsets',
            field=models.ManyToManyField(blank=True, related_name='quiz_event_part', to='classroom.QuizSet'),
        ),
        migrations.AlterField(
            model_name='quizevent',
            name='start_time',
            field=models.TimeField(blank=True, db_index=True, default=datetime.time(22, 13, 17, 820679)),
        ),
    ]
