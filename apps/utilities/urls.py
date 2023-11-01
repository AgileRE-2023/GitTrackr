from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('add_repository/', views.add_repository, name="add_repository"),
    path('detail_repository/', views.detail_repository, name="detail_repository"),
    path('history/', views.history, name="history")
]