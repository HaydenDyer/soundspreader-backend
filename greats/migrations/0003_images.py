# Generated by Django 3.2.8 on 2021-10-28 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greats', '0002_artist_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1_url', models.TextField(max_length=400)),
                ('img2_url', models.TextField(max_length=400)),
                ('img3_url', models.TextField(max_length=400)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='greats.artist')),
            ],
        ),
    ]
