# Generated by Django 3.1.3 on 2020-12-01 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='titel',
            new_name='title',
        ),
    ]
