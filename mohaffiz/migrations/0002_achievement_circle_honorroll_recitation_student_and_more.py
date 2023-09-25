# Generated by Django 4.2.4 on 2023-09-21 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mohaffiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='achievements/')),
                ('certificate_name', models.CharField(max_length=255)),
                ('certificate_image', models.ImageField(upload_to='certificates/')),
            ],
        ),
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mosque_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('work_schedule', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HonorRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_type', models.CharField(max_length=255)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.circle')),
            ],
        ),
        migrations.CreateModel(
            name='Recitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surah', models.CharField(max_length=255)),
                ('start_verse', models.PositiveIntegerField()),
                ('end_verse', models.PositiveIntegerField()),
                ('recitation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students/')),
                ('full_name', models.CharField(max_length=255)),
                ('national_id', models.CharField(max_length=14, unique=True)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('personal_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('guardian_mobile', models.CharField(max_length=15)),
                ('current_hifz', models.CharField(max_length=255)),
                ('combined_tests', models.TextField()),
                ('education_stage', models.CharField(max_length=255)),
                ('monthly_attendance', models.PositiveIntegerField(default=0)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.circle')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='teachers/')),
                ('full_name', models.CharField(max_length=255)),
                ('national_id', models.CharField(max_length=14, unique=True)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('personal_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('monthly_attendance', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_count', models.PositiveIntegerField()),
                ('initial_part_number', models.PositiveIntegerField()),
                ('final_part_number', models.PositiveIntegerField()),
                ('test_date', models.DateField()),
                ('result', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Mohaffiz',
        ),
        migrations.AddField(
            model_name='recitation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.student'),
        ),
        migrations.AddField(
            model_name='honorroll',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.student'),
        ),
        migrations.AddField(
            model_name='honorroll',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.teacher'),
        ),
        migrations.AddField(
            model_name='circle',
            name='supervisor_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.teacher'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='students',
            field=models.ManyToManyField(related_name='achievements', to='mohaffiz.student'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mohaffiz.teacher'),
        ),
    ]
