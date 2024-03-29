# Generated by Django 4.2 on 2024-02-20 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0004_rename_image_product_icon_alter_imagegallery_product_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="products.category",
            ),
        ),
    ]
