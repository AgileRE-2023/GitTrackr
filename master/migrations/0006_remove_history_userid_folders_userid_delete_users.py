# Generated by Django 4.2.5 on 2023-11-13 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0015_rename_extra_data_new_usersocialauth_extra_data'),
        ('master', '0005_folders_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='UserID',
        ),
        migrations.AddField(
            model_name='folders',
            name='UserID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='social_django.usersocialauth'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
