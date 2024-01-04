# steps.py

from behave import given, when, then
from master.models import Folder, Repository

@given('I am on "{url}" page for folder "{folder_name}"')
def step_impl(context, url, folder_name):
    context.browser.visit(url)
    context.folder = Folder.objects.get(name=folder_name)

@when('I fill in "Repository Name" with "{repo_name}" and submit the form')
def step_impl(context, repo_name):
    context.browser.fill('repository_name', repo_name)
    context.browser.find_by_value('Submit').first.click()

@then('I should be redirected to "{url}"')
def step_impl(context, url):
    assert context.browser.url == url

@then('I should see "{repo_name}" in the list of repositories')
def step_impl(context, repo_name):
    assert repo_name in context.browser.html

@when('I press "Add to my folder" button for "{repo_name}"')
def step_impl(context, repo_name):
    context.browser.find_by_text(f'Add {repo_name} to my folder').first.click()

@then('the database should have "{repo_name}" associated with "{folder_name}"')
def step_impl(context, repo_name, folder_name):
    folder = Folder.objects.get(name=folder_name)
    repo = Repository.objects.get(name=repo_name)
    assert repo in folder.repositories.all()

@then('I should see "{message}" message')
def step_impl(context, message):
    assert message in context.browser.html

@given('"{repo_name}" repository is added to "{folder_name}" folder')
def step_impl(context, repo_name, folder_name):
    folder = Folder.objects.get(name=folder_name)
    repo, created = Repository.objects.get_or_create(name=repo_name)
    folder.repositories.add(repo)

@when('I press "X" button next to "{repo_name}"')
def step_impl(context, repo_name):
    context.browser.find_by_text(f'Remove {repo_name}').first.click()

@then('"{repo_name}" should be removed from "{folder_name}" in the database')
def step_impl(context, repo_name, folder_name):
    folder = Folder.objects.get(name=folder_name)
    repo = Repository.objects.get(name=repo_name)
    assert repo not in folder.repositories.all()

@when('I fill in "Repository Name" with "{repo_name}"')
def step_impl(context, repo_name):
    context.browser.fill('repository_name', repo_name)

@when('I press "Add to my folder" button')
def step_impl(context):
    context.browser.find_by_value('Add to my folder').first.click()

@then('the response should contain "{message}"')
def step_impl(context, message):
    assert message in context.browser.html

@then('the "List Repository" field should not contain "{repo_name}"')
def step_impl(context, repo_name):
    assert repo_name not in context.browser.find_by_id('list_repository').text
