from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class HomeView(ListView):
    template_name = "trackr_app/index.html"
    
    def get_queryset(self):
        return

class StatRepo(ListView):
    template_name = "trackr_app/stat.html"

    def get_queryset(self):
        return