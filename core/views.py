from django.shortcuts import render
from django.views.generic.base import View

from accounts.models import SystemUser


class DashboardView(View):
    template_name = "core/dashboard.html"
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        context = {
            "total_active_user": SystemUser.objects.filter(is_active=True).count()
        }
        return render(request, self.template_name, context)
