# Generated by Django 3.2.10 on 2022-02-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_api', '0002_person_network_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(to='network_api.Friend'),
        ),
    ]
