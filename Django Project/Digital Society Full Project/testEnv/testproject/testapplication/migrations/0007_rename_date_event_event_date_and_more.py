# Generated by Django 5.1.4 on 2025-01-20 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapplication', '0006_complaint_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='event_time',
        ),
    ]
