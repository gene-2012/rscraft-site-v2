# Generated by Django 4.2.14 on 2024-07-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_backup'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='github_download_link',
            field=models.URLField(default='https://github.com/RedstoneCraftTeam/Redstone_Craft/releases/'),
            preserve_default=False,
        ),
    ]
