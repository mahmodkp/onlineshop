# Generated by Django 4.2 on 2024-02-22 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_remove_videogallery_product_delete_imagegallery_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
