# Generated by Django 3.2.10 on 2022-02-08 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='surname',
        ),
    ]
