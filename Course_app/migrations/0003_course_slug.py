# Generated by Django 5.0.2 on 2024-03-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0002_remove_codeexercise_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
