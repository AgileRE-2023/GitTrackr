from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def add_repository(request):
    return render(request, 'utilities/add_repository.html')

def detail_repository(request):
    return render(request, 'utilities/detail_repository.html')

def history(request):
    return render(request, 'utilities/history.html')