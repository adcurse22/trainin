# Generated by Django 4.2.7 on 2023-12-16 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_name_exercise_имя'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='имя',
            new_name='name',
        ),
    ]
