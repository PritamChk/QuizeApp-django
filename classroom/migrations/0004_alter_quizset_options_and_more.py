# Generated by Django 4.0.2 on 2022-02-14 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_rename_options_option'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizset',
            options={'ordering': ['-created_at', 'difficulty_level']},
        ),
        migrations.RenameField(
            model_name='quizset',
            old_name='dificulty_level',
            new_name='difficulty_level',
        ),
    ]
