# Generated by Django 5.0.3 on 2024-03-11 21:07

import content_sharing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_sharing', '0003_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to=content_sharing.models.user_directory_path),
        ),
    ]
