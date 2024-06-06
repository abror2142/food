# Generated by Django 5.0.6 on 2024-06-06 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.food'),
            preserve_default=False,
        ),
    ]
