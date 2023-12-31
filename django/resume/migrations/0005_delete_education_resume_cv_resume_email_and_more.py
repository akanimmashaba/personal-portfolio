# Generated by Django 4.2.6 on 2023-11-05 12:11

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_remove_project_tech'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.AddField(
            model_name='resume',
            name='cv',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='cv'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='resume',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='selfie'),
        ),
        migrations.AddField(
            model_name='resume',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='resume',
            name='professional_summary',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
