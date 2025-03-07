# Generated by Django 3.0.6 on 2020-06-08 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_invite_job'),
        ('jobs', '0022_job_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='invite',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='users.Invite'),
        ),
    ]
