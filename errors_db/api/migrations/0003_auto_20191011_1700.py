# Generated by Django 2.2.5 on 2019-10-11 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_error'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Error',
            new_name='ErrorInstance',
        ),
    ]