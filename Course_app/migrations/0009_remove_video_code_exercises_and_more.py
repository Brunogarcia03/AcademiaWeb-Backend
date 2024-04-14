# Generated by Django 5.0.2 on 2024-03-06 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0008_remove_video_code_exercises_and_more'),
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
            model_name='codeexercise',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Course_app.video'),
        ),
        migrations.AddField(
            model_name='questionexercise',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Course_app.video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course_app.course'),
        ),
    ]
