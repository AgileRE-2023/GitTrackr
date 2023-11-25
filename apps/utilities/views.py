from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from github import Github

from .forms import AddRepositoryForm
from master.models import Repository, Folders

import requests
import json

@login_required
def repository_detail(request, repository_id):
    # Mendapatkan repositori dari database
    repo = Repository.objects.get(RepositoryID=repository_id)

    # Membuat instance Github
    g = Github(settings.GITHUB_TOKEN)

    # Mendapatkan repositori dari GitHub
    github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")

    # Mendapatkan detail repositori
    details = {
        'Repository_Name': repo.Repository_Name,
        'Owner_Name': repo.Owner,
        'About': github_repo.description,
        'Languages': github_repo.get_languages(),
        'File_Size': github_repo.size,
        'Date_Created': github_repo.created_at,
        'Topics': github_repo.get_topics(),
        'Branch': github_repo.default_branch,
        'Contributors': [contributor.login for contributor in github_repo.get_contributors()],
        'Stars': github_repo.stargazers_count,
    }

    return render(request, 'utilities/repository_detail.html', {'details': details, 'repository_id': repository_id})

@login_required
def history(request):
    folders = Folders.objects.filter(UserID=request.user)
    return render(request, 'utilities/history.html', {'folders': folders})

@login_required
def add_repository(request, folder_id=None):
    if folder_id is not None:
        request.session['current_folder_id'] = folder_id

    folder_id = request.session.get('current_folder_id')
    folder = Folders.objects.get(FolderID=folder_id)

    form = AddRepositoryForm()
    folders = Folders.objects.all()
    return render(request, 'utilities/add_repository.html', {'form': form, 'folder': folder, 'folders': folders})

@login_required
def search_repository(request):
    if request.method == 'POST':
        form = AddRepositoryForm(request.POST)
        if form.is_valid():
            repository_name = form.cleaned_data['repository_name']

            headers = {'Authorization': f'token {settings.GITHUB_TOKEN}'}
            url = f'https://api.github.com/search/repositories?q={repository_name}'

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                form = AddRepositoryForm()
                data = response.json()
                repositories = data.get('items', [])
                folders = Folders.objects.all()
                
                folder_id = request.session.get('current_folder_id')
                folder = Folders.objects.get(FolderID=folder_id)
                
                return render(request, 'utilities/add_repository.html', {'form': form,'repositories': repositories, 'folders': folders, 'folder': folder})
            else:
                print(f'Error {response.status_code}: {response.text}')

    return redirect('add_repository')

@login_required
def save_repository(request):
    if request.method == 'POST':
        full_repository_name = request.POST.get('repository_name')
        repository_url = request.POST.get('repository_url')
        folder_id = request.session.get('current_folder_id')

        owner, repository_name = full_repository_name.split('/')

        if Repository.objects.filter(Repository_Name=repository_name, Folder_ID_id=folder_id, Url=repository_url).exists():
            messages.error(request, 'Repositori ini sudah ada di folder ini.')
            return redirect('add_repository_with_folder', folder_id=folder_id)

        repository = Repository(Owner=owner, Repository_Name=repository_name, Url=repository_url, Folder_ID_id=folder_id)
        repository.save()

    return redirect('add_repository_with_folder', folder_id=folder_id)

def five_repository(request):
    saved_repositories = Repository.objects.all()[:5]  # Retrieve the first 5 repositories
    return render(request, 'add_repository.html', {'saved_repositories': saved_repositories})
