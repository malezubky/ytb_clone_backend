# Generated by Django 4.2.3 on 2023-09-03 13:41

import base.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("base", "0013_delete_processedvideo"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProcessedVideo",
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
                ("video_title", models.CharField(max_length=200, unique=True)),
                ("video_description", models.CharField(max_length=600)),
                (
                    "video_file",
                    models.FileField(
                        upload_to="processed_videos/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4"]
                            ),
                            base.models.validate_video_size,
                        ],
                    ),
                ),
                (
                    "thumbnail_file",
                    models.FileField(
                        upload_to="thumbnails/",
                        validators=[base.models.validate_webp_format],
                    ),
                ),
            ],
        ),
    ]
