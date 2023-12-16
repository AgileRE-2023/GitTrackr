from django.shortcuts import render
from github import Github
from master.models import Repository, Folders

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.core.cache import cache

from master.models import Repository, Folders

import threading
import datetime
import requests
import json

# Create your views here.
from github import Github

@login_required
def compare_repositories(request, folder_id):
    g = Github(settings.GITHUB_TOKEN)

    folder_id = request.session.get('current_folder_id', folder_id)
    folder = Folders.objects.get(FolderID=folder_id)
    repositories = Repository.objects.filter(Folder_ID_id=folder_id)

    def fetch_repo_data(repo):
        cache_key = f"repo_data_{repo.RepositoryID}"
        repo_data = cache.get(cache_key)

        if not repo_data:
            github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")

            merged_pull_requests = 0
            for pr in github_repo.get_pulls(state='closed'):
                if pr.is_merged():
                    merged_pull_requests += 1
            
            closed_pull_requests = github_repo.get_pulls(state='closed').totalCount
            rejected_pull_requests = closed_pull_requests - merged_pull_requests

            repo_data = {
                'repo': repo,  
                'Repository_Name': repo.Repository_Name,
                'Commit': github_repo.get_commits().totalCount,
                'Merged_Pull_Request': merged_pull_requests,
                'Rejected_Pull_Request': rejected_pull_requests,
                'Contributors': github_repo.get_contributors().totalCount,
                'Languages': len(github_repo.get_languages()),
                'Forks': github_repo.forks_count,
                'Stars': github_repo.stargazers_count,
                'Last_Updated': github_repo.updated_at,
            }

            cache.set(cache_key, repo_data, 3600) 

        return repo_data

    threads = []
    stats = []

    for repo in repositories:
        thread = threading.Thread(target=lambda repo=repo: stats.append(fetch_repo_data(repo)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return render(request, 'comparison/compare_repository.html', {'stats': stats, 'folder': folder})


@login_required
def developer_statistic(request, repository_id):
    g = Github(settings.GITHUB_TOKEN)

    repo = Repository.objects.get(RepositoryID=repository_id)
    github_repo = g.get_repo(f"{repo.Owner}/{repo.Repository_Name}")
    
    repository_name = repo.Repository_Name
    owner_name = repo.Owner

    cache_key = f"developer_stats_{repo.RepositoryID}"
    developer_stats = cache.get(cache_key)

    if not developer_stats:
        contributors_stats = github_repo.get_stats_contributors()
        if not contributors_stats: 
            return render(request, 'comparison/developer_statistic.html', {
                'stats': None,
                'repository_name': repository_name, 
                'owner_name': owner_name
            })

        def fetch_contributor_data(contributor):
            pull_requests = g.search_issues(query=f'repo:{repo.Owner}/{repo.Repository_Name} type:pr author:{contributor.author.login}').totalCount
            issues = g.search_issues(query=f'repo:{repo.Owner}/{repo.Repository_Name} type:issue author:{contributor.author.login}').totalCount

            commits = list(github_repo.get_commits(author=contributor.author.login))
            additions = sum(c.stats.additions for c in commits)
            deletions = sum(c.stats.deletions for c in commits)

            first_contribution = commits[-1].commit.committer.date if commits else None
            last_contribution = commits[0].commit.committer.date if commits else None

            if len(commits) > 1:
                time_deltas = [(commits[i-1].commit.committer.date - commits[i].commit.committer.date) for i in range(1, len(commits))]
                average_time_between_commits = sum(time_deltas, datetime.timedelta(0)) / len(time_deltas)
                average_time_between_commits = int(average_time_between_commits.total_seconds() / 3600)  # Membulatkan ke jam terdekat
            else:
                average_time_between_commits = None

            return {
                'Developer_Name': contributor.author.login,
                'Commit': len(commits),
                'Additions': additions,
                'Deletions': deletions,
                'Pull_Requests': pull_requests,
                'Issues': issues,
                'First_Contribution': first_contribution.strftime('%d-%m-%Y') if first_contribution else None,
                'Last_Contribution': last_contribution.strftime('%d-%m-%Y') if last_contribution else None,
                'Average_Time_Between_Commits': average_time_between_commits,
            }

        threads = []
        developer_stats = []

        for contributor in contributors_stats:
            thread = threading.Thread(target=lambda contrib=contributor: developer_stats.append(fetch_contributor_data(contrib)))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        cache.set(cache_key, developer_stats, 3600)

    return render(request, 'comparison/developer_statistic.html', {
        'stats': developer_stats,
        'repository_name': repository_name, 
        'owner_name': owner_name
    })

