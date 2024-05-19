from django.db import models

__author__ = "Shafikur Rahman"

from core.models import Audit, Key, Timestamp


class TransactionCategory(Key, Timestamp, Audit):
    name = models.CharField(max_length=50, blank=False, null=False)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = "wallets"
        db_table = "transaction_categories"
        ordering = ["-added_at"]
        verbose_name = "Transaction Category"
        verbose_name_plural = "Transaction Categories"

    def __str__(self):
        if self.parent:
            return f"{self.code} - {self.name} --> {self.parent}"
        return f"{self.code} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.code:
            super().save(*args, **kwargs)
            self.code = f"TC-{self.pk:06d}"
            kwargs["force_insert"] = False
        super().save(*args, **kwargs)
