# Generated by Django 5.1.1 on 2024-10-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_laptop_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="laptop",
            name="display_size",
            field=models.IntegerField(default=15.6),
        ),
        migrations.AddField(
            model_name="laptop",
            name="ram",
            field=models.IntegerField(default=8),
        ),
    ]
