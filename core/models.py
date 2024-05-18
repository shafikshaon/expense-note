from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class Base(models.Model):
    class Meta:
        abstract = True


class Timestamp(Base):
    added_at = models.DateTimeField(auto_now_add=True, editable=False)
    changed_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        abstract = True


class Key(Base):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, null=False, blank=True)

    class Meta:
        abstract = True


class Audit(Base):
    is_deleted = models.BooleanField(default=False, null=False, blank=False)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name="%(app_label)s_%(class)s_added_by",
        null=True,
        blank=True,
    )
    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name="%(app_label)s_%(class)s_changed_by",
        null=True,
        blank=True,
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name="%(app_label)s_%(class)s_deleted_by",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
