# Generated by Django 3.2.8 on 2021-10-30 21:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soundspreader', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
