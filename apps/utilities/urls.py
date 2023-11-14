from django.contrib import admin
from django.urls import path, include
from . import views
from .views import add_repository, search_repository, save_repository, add_repository, five_repository

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('detail_repository/', views.detail_repository, name="detail_repository"),
    path('history/', views.history, name="history"),

    path('add_repository/', add_repository, name='add_repository'),
    path('search_repository/', search_repository, name='search_repository'),
    path('save_repository/', save_repository, name='save_repository'),
    path('five-repository/', five_repository, name='five_repository'),
]