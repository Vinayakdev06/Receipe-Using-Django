# Generated by Django 5.0.4 on 2024-07-23 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_subject_subjectmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rank', models.IntegerField()),
                ('date_of_report_card_generation', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='vege.student')),
            ],
            options={
                'unique_together': {('student', 'date_of_report_card_generation')},
            },
        ),
    ]