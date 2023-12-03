from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('repository_detail/<int:repository_id>/', views.repository_detail, name='repository_detail'),
    
    path('history/', views.history, name="history"),
    path('add_repository/<int:folder_id>/', views.add_repository, name='add_repository_with_folder'),
    path('search_repository/', views.search_repository, name='search_repository'),
    path('save_repository/', views.save_repository, name='save_repository'),
    path('five-repository/', views.five_repository, name='five_repository'),
]