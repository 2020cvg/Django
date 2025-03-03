# Generated by Django 3.0.6 on 2020-06-07 20:39

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_job_employee'),
        ('users', '0003_auto_20200606_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('message', ckeditor.fields.RichTextField(blank=True)),
                ('unread', models.BooleanField(default=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='jobs.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
