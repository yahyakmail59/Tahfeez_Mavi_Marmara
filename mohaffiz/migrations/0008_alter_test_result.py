# Generated by Django 4.2.4 on 2023-09-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mohaffiz', '0007_alter_achievement_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='result',
            field=models.IntegerField(),
        ),
    ]