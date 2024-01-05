from django.shortcuts import render
from github import Github
from master.models import Repository, Folders

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

import datetime
import requests
import json

# Create your views here.
from github import Github

@login_required
def compare_repositories(request, folder_id):
    g = Github(settings.GITHUB_TOKEN)

    if folder_id is not None:
        request.session['current_folder_id'] = folder_id

    folder_id = request.session.get('current_folder_id')
    folder = Folders.objects.get(FolderID=folder_id)

    repositories = Repository.objects.filter(Folder_ID_id=folder_id)

    stats = []

    for repo in repositories:
        github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")

        merged_pull_requests = 0
        rejected_pull_requests = 0
        for pr in github_repo.get_pulls(state='closed'):
            if pr.is_merged():
                merged_pull_requests += 1
            else:
                rejected_pull_requests += 1

        stats.append({
            'repo': repo,  
            'Repository_Name': repo.Repository_Name,
            'Owner_Name': repo.Owner,
            'Topics' : github_repo.get_topics(),
            'Commit': github_repo.get_commits().totalCount,
            'Merged_Pull_Request': merged_pull_requests,  
            'Rejected_Pull_Request': rejected_pull_requests,  
            'Contributors': github_repo.get_contributors().totalCount,
            'Languages': len(github_repo.get_languages()),
            'Forks': github_repo.forks_count,
            'Stars': github_repo.stargazers_count,
            'Last_Updated': github_repo.updated_at,
        })

    return render(request, 'comparison/compare_repository.html', {'stats': stats, 'folder': folder})

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
        # Mendapatkan jumlah pull request dan issue yang dibuat oleh kontributor
        pull_requests = g.search_issues(query=f'repo:{repo.Owner}/{repo.Repository_Name} type:pr author:{contributor.author.login}').totalCount
        issues = g.search_issues(query=f'repo:{repo.Owner}/{repo.Repository_Name} type:issue author:{contributor.author.login}').totalCount

        # Mendapatkan semua commit dari kontributor
        commits = [c for c in github_repo.get_commits(author=contributor.author.login)]

        # Mendapatkan waktu kontribusi pertama dan terakhir
        first_contribution = commits[-1].commit.committer.date.strftime('%d/%m/%Y')  # Waktu kontribusi pertama
        last_contribution = commits[0].commit.committer.date.strftime('%d/%m/%Y')  # Waktu kontribusi terakhir

        # Menghitung rata-rata waktu antara commit
        if len(commits) > 1:
            time_deltas = [(commits[i-1].commit.committer.date - commits[i].commit.committer.date) for i in range(1, len(commits))]
            average_time_between_commits = sum(time_deltas, datetime.timedelta(0)) / len(time_deltas)
            average_time_between_commits = round(average_time_between_commits.total_seconds() / 3600, 1)  # Ubah baris ini
        else:
            average_time_between_commits = None

        # Menambahkan data ke list stats
        stats.append({
            'Developer_Name': contributor.author.login,
            'Commit': contributor.total,
            'Additions': sum(week.a for week in contributor.weeks),
            'Deletions': sum(week.d for week in contributor.weeks),
            'Pull_Requests': pull_requests,  # Tambahkan baris ini
            'Issues': issues,  # Tambahkan baris ini
            'First_Contribution': first_contribution,  # Tambahkan baris ini
            'Last_Contribution': last_contribution,  # Tambahkan baris ini
            'Average_Time_Between_Commits': average_time_between_commits,  # Tambahkan baris ini
        })

    return render(request, 'comparison/developer_statistic.html', {'stats': stats})

@login_required
def compare(request):
    folders = Folders.objects.filter(UserID=request.user)
    return render(request, 'comparison/compare_repository.html', {'folders': folders})