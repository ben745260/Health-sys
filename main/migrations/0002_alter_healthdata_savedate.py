# Generated by Django 4.1.1 on 2022-10-08 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='saveDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]