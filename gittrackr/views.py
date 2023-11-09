from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base/home_unlogged.html")

def indexLogged(request):
    return render(request, "base/home_logged.html")

