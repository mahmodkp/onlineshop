# Generated by Django 4.2 on 2024-02-21 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_comment_article_alter_imagegallery_article_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MediaFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("media", models.FileField(null=True, upload_to="gallery_file_path")),
                (
                    "media_type",
                    models.IntegerField(
                        choices=[(1, "image"), (2, "video"), (3, "audio")], null=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="blog.article",
                    ),
                ),
            ],
        ),
    ]