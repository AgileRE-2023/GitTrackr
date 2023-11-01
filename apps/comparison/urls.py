from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('compare_repository/', views.compare_repository, name="compare_repository"),
    path('developer_statistic/', views.developer_statistic, name="developer_statistic")
]