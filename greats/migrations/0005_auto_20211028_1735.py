# Generated by Django 3.2.8 on 2021-10-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greats', '0004_artist_imgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='imgs',
        ),
        migrations.AddField(
            model_name='artist',
            name='img1url',
            field=models.TextField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='img2url',
            field=models.TextField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='img3url',
            field=models.TextField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
