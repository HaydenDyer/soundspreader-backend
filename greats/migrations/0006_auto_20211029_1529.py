# Generated by Django 3.2.8 on 2021-10-29 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greats', '0005_auto_20211028_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='img1url',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='img2url',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='img3url',
        ),
    ]
