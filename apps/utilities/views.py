# Create your views here.
from django.shortcuts import render, redirect
from .forms import AddRepositoryForm
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from master.models import Repository

# Create your views here.

def detail_repository(request):
    return render(request, 'utilities/detail_repository.html')

def history(request):
    return render(request, 'utilities/history.html')

def add_repository(request):
    form = AddRepositoryForm()
    return render(request, 'utilities/add_repo.html', {'form': form})

def dashboard(request):
    return render(request, 'utilities/dashboard.html')

@login_required
def search_repository(request):
    if request.method == 'POST':
        form = AddRepositoryForm(request.POST)
        if form.is_valid():
            repository_name = form.cleaned_data['repository_name']

            # Gunakan personal access token atau OAuth token untuk mengotentikasi permintaan ke GitHub API
            headers = {'Authorization': f'token {settings.GITHUB_TOKEN}'}
            url = f'https://api.github.com/search/repositories?q={repository_name}'

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                repositories = data.get('items', [])
                return render(request, 'utilities/repository_search_results.html', {'repositories': repositories})
            else:
                print(f'Error {response.status_code}: {response.text}')

    return redirect('add_repository')

@login_required
def save_repository(request):
    if request.method == 'POST':
        repository_name = request.POST.get('repository_name')

        # Gunakan user yang sudah login
        user = request.user

        # Simpan repository ke dalam database
        repository = Repository(Repository_Name=repository_name)
        repository.save()

    return redirect('dashboard')