from django.contrib import admin

from wallets.models import Wallet, TransactionCategory

admin.site.register(Wallet)
admin.site.register(TransactionCategory)
