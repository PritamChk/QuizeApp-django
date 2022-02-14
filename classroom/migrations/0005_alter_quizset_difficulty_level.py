# Generated by Django 4.0.2 on 2022-02-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_alter_quizset_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizset',
            name='difficulty_level',
            field=models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='E', max_length=2),
        ),
    ]