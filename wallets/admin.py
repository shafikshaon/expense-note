from django.contrib import admin

from wallets.models import Wallet, TransactionCategory, Transaction

admin.site.register(Wallet)
admin.site.register(TransactionCategory)
admin.site.register(Transaction)
