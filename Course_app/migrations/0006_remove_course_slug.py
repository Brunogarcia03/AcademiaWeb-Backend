# Generated by Django 5.0.2 on 2024-03-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0005_alter_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
    ]
