# Generated by Django 3.0.6 on 2020-06-05 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20200606_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='employee',
        ),
    ]
