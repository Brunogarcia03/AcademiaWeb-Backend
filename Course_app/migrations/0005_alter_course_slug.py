# Generated by Django 5.0.2 on 2024-03-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0004_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
