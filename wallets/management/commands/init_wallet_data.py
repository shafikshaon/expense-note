__author__ = "Shafikur Rahman"

import random

from django.core.management.base import BaseCommand

from accounts.models.system_user import SystemUser
from wallets.models.wallet import Wallet
from wallets.models.transaction import Transaction
from wallets.models.transaction_category import TransactionCategory


class Command(BaseCommand):
    help = "Generate initial data for wallets"

    def handle(self, *args, **kwargs):
        # Get the system user with the specified email
        user = SystemUser.objects.get(email="shafikshaon@gmail.com")

        # If the user does not exist, return
        if not user:
            return

        # Delete all existing transaction categories, transactions and wallets
        TransactionCategory.objects.all().delete()
        Wallet.objects.all().delete()
        Transaction.objects.all().delete()

        # Create expense category
        expense, created = TransactionCategory.objects.get_or_create(
            name="EXPENSE", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Food & Beverage", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Transportation", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="House Rent", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Phone Bill", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Electricity Bill", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Gas Bill", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Internet Bill", added_by=user
        )
        TransactionCategory.objects.create(
            parent=expense, name="Donations", added_by=user
        )
        TransactionCategory.objects.create(parent=expense, name="Gifts", added_by=user)

        # Create income category
        income, created = TransactionCategory.objects.get_or_create(
            name="INCOME", added_by=user
        )
        TransactionCategory.objects.create(parent=income, name="Salary", added_by=user)
        TransactionCategory.objects.create(
            parent=income, name="Cashback", added_by=user
        )

        # Create debt/loan category
        loan, created = TransactionCategory.objects.get_or_create(
            name="LOAN", added_by=user
        )
        TransactionCategory.objects.create(
            parent=loan, name="Debt Collection", added_by=user
        )
        TransactionCategory.objects.create(
            parent=loan, name="Loan Repayment", added_by=user
        )
        TransactionCategory.objects.create(parent=loan, name="Debt", added_by=user)
        TransactionCategory.objects.create(parent=loan, name="Loan", added_by=user)

        # Create investment category
        investment, created = TransactionCategory.objects.get_or_create(
            name="INVESTMENT", added_by=user
        )
        TransactionCategory.objects.create(
            parent=investment, name="Mutual Fund", added_by=user
        )
        TransactionCategory.objects.create(parent=investment, name="DPS", added_by=user)
        TransactionCategory.objects.create(parent=investment, name="FDR", added_by=user)

        # Create credit category
        credit, created = TransactionCategory.objects.get_or_create(
            name="CREDIT", added_by=user
        )
        TransactionCategory.objects.create(
            parent=credit, name="Credit Card", added_by=user
        )

        # Create goal category
        goal, created = TransactionCategory.objects.get_or_create(
            name="GOAL", added_by=user
        )
        TransactionCategory.objects.create(
            parent=goal, name="Buy Electronics", added_by=user
        )
        TransactionCategory.objects.create(
            parent=goal, name="Buy Property", added_by=user
        )
        TransactionCategory.objects.create(
            parent=goal, name="Emergency Fund", added_by=user
        )

        # Create investment category
        investment, created = TransactionCategory.objects.get_or_create(
            name="INVESTMENT", added_by=user
        )
        TransactionCategory.objects.create(
            parent=investment, name="Savings", added_by=user
        )

        # Create wallets and assign categories
        bbl_debit_account, created = Wallet.objects.get_or_create(
            name="BBL Debit Account", currency="BDT", wallet_type="Basic", added_by=user
        )
        ebl_debit_account, created = Wallet.objects.get_or_create(
            name="EBL Debit Account", currency="BDT", wallet_type="Basic", added_by=user
        )
        money_bag, created = Wallet.objects.get_or_create(
            name="Money Bag", currency="BDT", wallet_type="Basic", added_by=user
        )
        nagad, created = Wallet.objects.get_or_create(
            name="Nagad", currency="BDT", wallet_type="Basic", added_by=user
        )
        upay, created = Wallet.objects.get_or_create(
            name="Upay", currency="BDT", wallet_type="Basic", added_by=user
        )
        rocket, created = Wallet.objects.get_or_create(
            name="Rocket", currency="BDT", wallet_type="Basic", added_by=user
        )
        bkash, created = Wallet.objects.get_or_create(
            name="bKash", currency="BDT", wallet_type="Basic", added_by=user
        )
        scb_debit_account, created = Wallet.objects.get_or_create(
            name="SCB Debit Account", currency="BDT", wallet_type="Basic", added_by=user
        )
        scb_credit_card, created = Wallet.objects.get_or_create(
            name="SCB Credit Card", currency="BDT", wallet_type="Credit", added_by=user
        )
        bbl_credit_card, created = Wallet.objects.get_or_create(
            name="BBL Credit Card", currency="BDT", wallet_type="Credit", added_by=user
        )
        idlc, created = Wallet.objects.get_or_create(
            name="IDLC", currency="BDT", wallet_type="Investment", added_by=user
        )
        bbl_dps, created = Wallet.objects.get_or_create(
            name="BBL DPS", currency="BDT", wallet_type="Investment", added_by=user
        )
        bkash_savings, created = Wallet.objects.get_or_create(
            name="bKash Savings",
            currency="BDT",
            wallet_type="Investment",
            added_by=user,
        )

        # Assign transaction categories
        goal_categories = TransactionCategory.objects.filter(parent__name="GOAL")
        investment_categories = TransactionCategory.objects.filter(
            parent__name="INVESTMENT"
        )
        income_categories = TransactionCategory.objects.filter(parent__name="INCOME")
        expense_categories = TransactionCategory.objects.filter(parent__name="EXPENSE")
        credit_categories = TransactionCategory.objects.filter(parent__name="CREDIT")

        joined_categories = (
            goal_categories.union(investment_categories)
            .union(income_categories)
            .union(expense_categories)
        )
        bbl_debit_account.category.set(joined_categories)
        ebl_debit_account.category.set(joined_categories)
        money_bag.category.set(joined_categories)
        nagad.category.set(joined_categories)
        bkash.category.set(joined_categories)
        upay.category.set(joined_categories)
        rocket.category.set(joined_categories)
        scb_debit_account.category.set(joined_categories)

        bkash_savings.category.set(investment_categories)
        bbl_dps.category.set(investment_categories)
        idlc.category.set(investment_categories)

        bbl_credit_card.category.set(credit_categories)
        scb_credit_card.category.set(credit_categories)

        categories = list(TransactionCategory.objects.exclude(parent__isnull=False))
        wallets = list(Wallet.objects.all())
        for i in range(500):
            random_category = random.choice(categories) if categories else None
            wallet = random.choice(wallets) if wallets else None
            random_decimal = round(random.uniform(1.00, 100.00), 2)

            Transaction.objects.create(
                amount=random_decimal,
                category=random_category,
                wallet=wallet,
                added_by=user,
                date='2024-05-19'
            )

        print("Wallet data generated successfully.")
