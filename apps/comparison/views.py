from django.shortcuts import render
from django.http import JsonResponse
from github import Github

# Create your views here.
def compare_repository(request):
    return render(request, 'comparison/compare_repository.html')

def developer_statistic(request):
    return render(request, 'comparison/developer_statistic.html')


def get_github_developer_info(request, username, repo):
    access_token = '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'
    g = Github(access_token)
    
    try:
        repository = g.get_repo(f"{username}/{repo}")
        developers = repository.get_contributors()
        
        developer_info = []
        for developer in developers:
            developer_info.append({
                'login': developer.login,
                'avatar_url': developer.avatar_url,
                'contributions': developer.contributions,
                'html_url': developer.html_url,
            })
        
        return JsonResponse({'developers': developer_info})
    
    except Exception as e:
        return JsonResponse({'error': str(e)})