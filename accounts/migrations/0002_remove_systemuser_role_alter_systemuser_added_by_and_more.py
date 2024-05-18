# Generated by Django 5.0.6 on 2024-05-18 15:18

import core.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="systemuser",
            name="role",
        ),
        migrations.AlterField(
            model_name="systemuser",
            name="added_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET(core.models.get_sentinel_user),
                related_name="%(app_label)s_%(class)s_added_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="systemuser",
            name="changed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET(core.models.get_sentinel_user),
                related_name="%(app_label)s_%(class)s_changed_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="systemuser",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET(core.models.get_sentinel_user),
                related_name="%(app_label)s_%(class)s_deleted_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
