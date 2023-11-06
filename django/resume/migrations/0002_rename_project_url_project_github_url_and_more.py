# Generated by Django 4.2.6 on 2023-11-05 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_url',
            new_name='github_url',
        ),
        migrations.AddField(
            model_name='project',
            name='live_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]