# Generated by Django 4.2.4 on 2023-09-26 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mohaffiz', '0014_alter_test_test_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 26, 11, 31, 38, 897452), verbose_name='تاريخ الإختبار'),
        ),
    ]
