from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime, timedelta
from github import Github

from .forms import AddRepositoryForm
from master.models import Repository, Folders

import requests
import json

@login_required
def repository_detail(request, repository_id):
    repo = Repository.objects.get(RepositoryID=repository_id)

    g = Github(settings.GITHUB_TOKEN)

    github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")

    languages = github_repo.get_languages()
    total_bytes = sum(languages.values())
    formatted_languages = {lang: f"{(bytes / total_bytes) * 100:.1f}%" for lang, bytes in languages.items()}

    details = {
        'Repository_Name': repo.Repository_Name,
        'Owner_Name': repo.Owner,
        'About': github_repo.description,
        'Languages': formatted_languages,
        'File_Size': github_repo.size,
        'Date_Created': github_repo.created_at,
        'Topics': github_repo.get_topics(),
        'Branch': github_repo.default_branch,
        'Contributors': [contributor.login for contributor in github_repo.get_contributors()],
        'Stars': github_repo.stargazers_count,
        'CountCommit': json.dumps(get_github_data(github_repo)),
        'CountPullreq': json.dumps(count_pull_requests(github_repo)),
    }

    return render(request, 'utilities/repository_detail.html', {'details': details, 'repository_id': repository_id})


def get_github_data(repo):
    commit_count_data = {}

    for commit in repo.get_commits():
        timestamp = commit.commit.author.date.timestamp()
        commit_date = datetime.fromtimestamp(timestamp)
        month_year = commit_date.strftime('%Y-%m')
        contributor = commit.commit.author.name

        if month_year not in commit_count_data:
            commit_count_data[month_year] = {'total': 0, 'contributors': {}}

        commit_count_data[month_year]['total'] += 1

        if contributor not in commit_count_data[month_year]['contributors']:
            commit_count_data[month_year]['contributors'][contributor] = 1
        else:
            commit_count_data[month_year]['contributors'][contributor] += 1
        
    return commit_count_data

def count_pull_requests(repo):
    pull_requests = repo.get_pulls(state='all')
    pull_request_count_data = {}

    for pull_request in pull_requests:
        timestamp = pull_request.created_at.timestamp()
        pull_request_date = datetime.fromtimestamp(timestamp)
        month_year = pull_request_date.strftime('%Y-%m')
        contributor = pull_request.user.login

        if month_year not in pull_request_count_data:
            pull_request_count_data[month_year] = {'total': 0, 'contributors': {}}
        pull_request_count_data[month_year]['total'] += 1

        if contributor not in pull_request_count_data[month_year]['contributors']:
            pull_request_count_data[month_year]['contributors'][contributor] = 1
        else:
            pull_request_count_data[month_year]['contributors'][contributor] += 1

    return pull_request_count_data

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
            full_repository_name = form.cleaned_data['repository_name']

            headers = {'Authorization': f'token {settings.GITHUB_TOKEN}'}
            url = f'https://api.github.com/search/repositories?q={full_repository_name}'

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                form = AddRepositoryForm()
                data = response.json()
                repositories = data.get('items', [])

                for repository in repositories:
                    repository['repository_owner'], repository['repository_name'] = repository['full_name'].split('/')

                folders = Folders.objects.all()

                folder_id = request.session.get('current_folder_id')
                folder = Folders.objects.get(FolderID=folder_id)

                return render(request, 'utilities/add_repository.html', {'form': form, 'repositories': repositories, 'folders': folders, 'folder': folder})
            else:
                print(f'Error {response.status_code}: {response.text}')

    return redirect('add_repository')


@login_required
def save_repository(request):
    if request.method == 'POST':
        repository_name = request.POST.get('repository_name')
        owner = request.POST.get('repository_owner')
        repository_url = request.POST.get('repository_url')
        folder_id = request.session.get('current_folder_id')

        if Repository.objects.filter(Repository_Name=repository_name, Folder_ID_id=folder_id, Url=repository_url).exists():
            messages.error(request, 'Repositori ini sudah ada di folder ini.')
            return redirect('add_repository_with_folder', folder_id=folder_id)

        repository = Repository(Owner=owner, Repository_Name=repository_name, Url=repository_url, Folder_ID_id=folder_id)
        repository.save()

    return redirect('add_repository_with_folder', folder_id=folder_id)


def five_repository(request):
    saved_repositories = Repository.objects.all()[:5]
    return render(request, 'add_repository.html', {'saved_repositories': saved_repositories})