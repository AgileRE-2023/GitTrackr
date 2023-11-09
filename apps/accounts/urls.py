from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from apps.accounts import views

urlpatterns = [
    path("__reload__", include("django_browser_reload.urls")),
    path('login/', views.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
