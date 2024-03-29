# Generated by Django 5.0.3 on 2024-03-12 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_sharing', '0006_post_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_sharing.post')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_sharing.userprofile')),
            ],
        ),
    ]
