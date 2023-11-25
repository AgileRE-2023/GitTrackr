from django.shortcuts import render
from github import Github
from master.models import Repository, Folders

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

from master.models import Repository, Folders

import requests
import json

# Create your views here.
from github import Github

@login_required
def compare_repositories(request, folder_id):
    # Membuat instance Github
    g = Github(settings.GITHUB_TOKEN)

    repositories = Repository.objects.filter(Folder_ID_id=folder_id)

    stats = []

    for repo in repositories:
        # Mendapatkan repositori dari GitHub
        github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")

        # Menambahkan data ke list stats
        stats.append({
            'repo': repo,  # Tambahkan baris ini
            'Repository_Name': repo.Repository_Name,
            'Topics' : github_repo.get_topics(),
            'Commit': github_repo.get_commits().totalCount,
            'Pull_Request': github_repo.get_pulls(state='open', sort='created', base='master').totalCount,
            'Contributors': github_repo.get_contributors().totalCount,
            'Languages': len(github_repo.get_languages()),
            'Forks': github_repo.forks_count,
            'Stars': github_repo.stargazers_count,
            'Open_Issues': github_repo.get_issues(state='open'),
        })

    return render(request, 'comparison/compare_repository.html', {'stats': stats})



@login_required
def developer_statistic(request, repository_id):
    # Membuat instance Github
    g = Github(settings.GITHUB_TOKEN)

    # Mendapatkan repositori dari database
    repo = Repository.objects.get(RepositoryID=repository_id)

    # Mendapatkan repositori dari GitHub
    github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")

    stats = []

    # Mendapatkan statistik kontributor
    contributors_stats = github_repo.get_stats_contributors()

    for contributor in contributors_stats:
        # Menambahkan data ke list stats
        stats.append({
            'Developer_Name': contributor.author.login,
            'Commit': contributor.total,
            'Additions': sum(week.a for week in contributor.weeks),
            'Deletions': sum(week.d for week in contributor.weeks),
            'Forks': github_repo.forks_count,
            'Stars': github_repo.stargazers_count,
            'Open_Issues': github_repo.get_issues(state='open').totalCount,
        })

    return render(request, 'comparison/developer_statistic.html', {'stats': stats})