__author__ = "Shafikur Rahman"

from django.db import models

from core.models import Key, Timestamp, Audit

WALLET_TYPES = (
    ("Basic Wallet", "Basic"),
    ("Credit Wallet", "Credit"),
    ("Goal Wallet", "Goal"),
    ("Investment Wallet", "Investment"),
)

CURRENCY = (("BDT", "BDT"),)


class Wallet(Key, Timestamp, Audit):
    name = models.CharField(max_length=50, blank=False, null=False)
    currency = models.CharField(max_length=5, choices=CURRENCY, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    initial_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    exclude_from_total_balance = models.BooleanField(default=False)
    wallet_type = models.CharField(
        max_length=20, choices=WALLET_TYPES, blank=False, null=False
    )

    class Meta:
        app_label = "wallets"
        db_table = "wallets"
        ordering = ["-added_at"]
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"

    def __str__(self):
        return f"{self.code} - {self.name} - {self.currency} - {self.wallet_type}"

    def save(self, *args, **kwargs):
        if not self.code:
            super().save(*args, **kwargs)
            self.code = f"W-{self.pk:06d}"
            kwargs["force_insert"] = False
        super().save(*args, **kwargs)
