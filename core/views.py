from datetime import timedelta

from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import View

from accounts.models import SystemUser
from wallets.models import Transaction


class DashboardView(View):
    template_name = "core/dashboard.html"
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        # Calculate date range
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=7)

        # Query to get category-wise amount sum for the last 7 days
        category_sums = (
            Transaction.objects.filter(date__range=(start_date, end_date))
            .values('category__name')
            .annotate(total_amount=Sum('amount'))
            .order_by('category__name')
        )

        category_sum_labels = [entry['category__name'] for entry in category_sums]
        category_sum_amounts = [float(entry['total_amount']) for entry in category_sums]
        context = {
            "total_active_user": SystemUser.objects.filter(is_active=True).count(),
            "category_sum_labels": category_sum_labels,
            "category_sum_amounts": category_sum_amounts,
        }
        return render(request, self.template_name, context)
