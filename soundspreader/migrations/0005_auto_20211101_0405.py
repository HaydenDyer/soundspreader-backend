# Generated by Django 3.2.8 on 2021-11-01 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soundspreader', '0004_alter_post_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='songTitle',
        ),
    ]
