from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from .views import get_github_developer_info

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('compare_repositories/<int:folder_id>/', views.compare_repositories, name="compare_repositories"),
    path('developer_statistic/<int:repository_id>/', views.developer_statistic, name="developer_statistic")
]