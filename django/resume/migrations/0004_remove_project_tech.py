# Generated by Django 4.2.6 on 2023-11-05 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_project_tech'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tech',
        ),
    ]