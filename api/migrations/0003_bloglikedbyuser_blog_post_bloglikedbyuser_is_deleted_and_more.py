# Generated by Django 5.1 on 2024-08-20 06:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_bloglikedbyuser_publisher_blogpost_publisher"),
    ]

    operations = [
        migrations.AddField(
            model_name="bloglikedbyuser",
            name="blog_post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="liked_blogs",
                to="api.blogpost",
            ),
        ),
        migrations.AddField(
            model_name="bloglikedbyuser",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="bloglikedbyuser",
            name="name",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="bloglikedbyuser",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
