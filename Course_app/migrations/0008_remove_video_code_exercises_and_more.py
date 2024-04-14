# Generated by Django 5.0.2 on 2024-03-06 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0007_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='code_exercises',
        ),
        migrations.RemoveField(
            model_name='video',
            name='question_exercises',
        ),
        migrations.AddField(
            model_name='video',
            name='code_exercises',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Course_app.codeexercise'),
        ),
        migrations.AddField(
            model_name='video',
            name='question_exercises',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Course_app.questionexercise'),
        ),
    ]
