# Generated by Django 4.2.3 on 2023-07-25 19:29

import base.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("base", "0003_delete_processedvideo_delete_rawvideo"),
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
            ],
        ),
    ]
