import debug_toolbar
from decouple import config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import DashboardView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", DashboardView.as_view()),
]

if config("DEBUG", cast=bool, default=True):
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
