from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('', views.index),
    path('logged/', views.indexLogged, name="loggedHomepage"),
    path('accounts/', include('apps.accounts.urls')),
    path('comparison/', include('apps.comparison.urls')),
    path('utilities/', include('apps.utilities.urls')),
]