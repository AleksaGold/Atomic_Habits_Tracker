
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("habit.urls", namespace="habit")),
    path("", include("users.urls", namespace="users")),
]
