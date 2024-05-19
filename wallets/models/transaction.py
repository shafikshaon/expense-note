from django.db import models

__author__ = "Shafikur Rahman"

from core.models import Key, Timestamp, Audit
from wallets.models.wallet import Wallet
from wallets.models.transaction_category import TransactionCategory


class Transaction(Key, Timestamp, Audit):
    amount = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.0, blank=False, null=False
    )
    category = models.ForeignKey(
        TransactionCategory, on_delete=models.CASCADE, blank=False, null=False
    )
    wallet_type = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, blank=False, null=False
    )
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    note = models.TextField(blank=True, null=True)
    exclude_from_report = models.BooleanField(default=False)

    class Meta:
        app_label = "wallets"
        db_table = "transactions"
        ordering = ["-added_at"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.wallet_type.name} - {self.category.name} - {self.amount}"
