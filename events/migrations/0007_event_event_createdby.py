# Generated by Django 4.2.1 on 2023-06-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_participant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_createdby',
            field=models.CharField(default='', max_length=50),
        ),
    ]