# Generated by Django 3.2.8 on 2021-10-29 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greats', '0008_auto_20211029_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('years_active', models.CharField(max_length=16)),
                ('nationality', models.CharField(max_length=32)),
                ('bio', models.TextField(max_length=1600)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='greats.artist'),
            preserve_default=False,
        ),
    ]