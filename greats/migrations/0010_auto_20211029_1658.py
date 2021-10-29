# Generated by Django 3.2.8 on 2021-10-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greats', '0009_auto_20211029_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='nationality',
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
