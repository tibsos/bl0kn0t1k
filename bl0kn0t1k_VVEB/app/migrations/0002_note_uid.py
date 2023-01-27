# Generated by Django 4.1.4 on 2023-01-01 23:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
