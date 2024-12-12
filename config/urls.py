from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/lms/", permanent=False)),
    path("lms/", include("lms.urls", namespace="lms")),
    path("users/", include("users.urls", namespace="users")),
]
