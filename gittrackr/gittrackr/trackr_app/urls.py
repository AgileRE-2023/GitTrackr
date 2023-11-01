from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("stat",views.StatRepo.as_view(), name="StatRepo"),
]