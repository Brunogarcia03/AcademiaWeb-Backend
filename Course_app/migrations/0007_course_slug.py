# Generated by Django 5.0.2 on 2024-03-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0006_remove_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
