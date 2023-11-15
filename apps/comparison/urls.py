from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from .views import get_github_developer_info

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('compare_repository/', views.compare_repository, name="compare_repository"),
    path('developer_statistic/', views.developer_statistic, name="developer_statistic"),
    path('get_github_developer_info/<str:username>/<str:repo>/', get_github_developer_info, name='get_github_developer_info'),
]