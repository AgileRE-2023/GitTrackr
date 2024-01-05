from behave import given, when, then
from master.models import Repository

@given('I am on "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/" page')
def step_impl(context, repo_id):
    # Assume your Django app has a URL pattern for repository detail like "utilities/repository_detail/<repo_id>/"
    # You may need to use a library like splinter or selenium for browser automation
    context.browser.visit(f'http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/')

@when('I press "Developer Activity" button in the repository detail')
def step_impl(context):
    # Assume there is a button with class "developer-activity-button" for developer activity
    context.browser.find_by_css('.developer-activity-button').first.click()

@then('the response should contain "Show Developer Statistic Success"')
def step_impl(context):
    assert 'Show Developer Statistic Success' in context.browser.html

@then('I should be redirected to "http://127.0.0.1:8000/comparison/developer_statistic/{repo_id}/" page')
def step_impl(context, repo_id):
    assert context.browser.url == f'http://127.0.0.1:8000/comparison/developer_statistic/{repo_id}/'

@then('I should see "Comparison Table of Developer Statistics"')
def step_impl(context):
    assert 'Comparison Table of Developer Statistics' in context.browser.html

@then('the response should not contain "Show Success"')
def step_impl(context):
    assert 'Show Success' not in context.browser.html

@then('the response status code should be "{status_code}"')
def step_impl(context, status_code):
    assert context.browser.status_code == int(status_code)

@then('I should still be on "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/" page')
def step_impl(context, repo_id):
    assert context.browser.url == f'http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/'
