from django.shortcuts import render

# Create your views here.
def compare_repository(request):
    return render(request, 'comparison/compare_repository.html')

def developer_statistic(request):
    return render(request, 'comparison/developer_statistic.html')