# Generated by Django 4.2 on 2024-02-18 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_alter_product_options_category_created_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="image",
            new_name="icon",
        ),
        migrations.AlterField(
            model_name="imagegallery",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="videogallery",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="products.product",
            ),
        ),
    ]