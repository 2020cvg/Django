# Generated by Django 3.0.6 on 2020-05-30 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200530_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
    ]
