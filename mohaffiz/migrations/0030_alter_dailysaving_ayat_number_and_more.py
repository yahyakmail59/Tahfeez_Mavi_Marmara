# Generated by Django 4.2.4 on 2023-09-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mohaffiz', '0029_rename_start_verse_dailysaving_ayat_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailysaving',
            name='ayat_number',
            field=models.PositiveIntegerField(default='1', verbose_name='رقم آية البداية'),
        ),
        migrations.AlterField(
            model_name='dailysaving',
            name='ayat_number2',
            field=models.PositiveIntegerField(default='3', verbose_name='رقم آية النهاية'),
        ),
        migrations.AlterField(
            model_name='dailysaving',
            name='name',
            field=models.CharField(default='سُورَةُ ٱلْفَاتِحَةِ', max_length=100, verbose_name='اختر السورة'),
        ),
    ]
