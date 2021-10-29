# Generated by Django 3.2.8 on 2021-10-29 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greats', '0006_auto_20211029_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='years_active',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=24)),
                ('subject', models.CharField(max_length=32)),
                ('body', models.TextField(max_length=4000)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='greats.artist')),
            ],
        ),
    ]
