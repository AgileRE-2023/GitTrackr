# Generated by Django 4.2.5 on 2023-11-12 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_remove_repository_folderid_alter_folders_folderid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folders',
            name='UserID',
        ),
    ]
