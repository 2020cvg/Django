# Generated by Django 3.0.6 on 2020-06-08 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200609_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='job',
        ),
    ]
