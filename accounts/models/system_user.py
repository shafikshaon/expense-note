__author__ = "Shafikur Rahman"

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import Key, Timestamp, Audit


class SystemUser(AbstractUser, Key, Timestamp, Audit):
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        app_label = "accounts"
        db_table = "users"
        ordering = ["-added_at"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.code} - {self.username} - {self.get_full_name()}"

    def save(self, *args, **kwargs):
        if not self.code:
            super().save(*args, **kwargs)
            self.code = f"SU-{self.pk:06d}"
            kwargs["force_insert"] = False
        super().save(*args, **kwargs)
