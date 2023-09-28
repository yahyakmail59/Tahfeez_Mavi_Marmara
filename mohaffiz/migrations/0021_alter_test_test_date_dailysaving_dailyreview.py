# Generated by Django 4.2.4 on 2023-09-26 11:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mohaffiz', '0020_alter_test_final_part_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 26, 14, 17, 20, 979111), verbose_name='تاريخ الإختبار'),
        ),
        migrations.CreateModel(
            name='DailySaving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surah', models.CharField(choices=[('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس'), ('الناس', 'الناس')], max_length=100)),
                ('start_verse', models.PositiveIntegerField()),
                ('end_verse', models.PositiveIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.student', verbose_name='اختر الطالب')),
            ],
        ),
        migrations.CreateModel(
            name='DailyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surah_or_part', models.CharField(max_length=100)),
                ('start_verse', models.PositiveIntegerField()),
                ('end_verse', models.PositiveIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.student', verbose_name='اختر الطالب')),
            ],
        ),
    ]