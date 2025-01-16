# Generated by Django 4.1 on 2022-09-10 01:16

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='images/profile/defaultprofile.svg', max_length=256, upload_to=accounts.models.user_directory_path),
        ),
    ]
