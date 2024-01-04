from behave import given, when, then
from master.models import Folders, Repository

@given('I am on "{url}" page for folder "{folder_name}"')
def step_impl(context, url, folder_name):
    context.browser.visit(url)
    context.folder = Folders.objects.get(name=folder_name)

@given('folder "{folder_name}" has at least two repositories added')
def step_impl(context, folder_name):
    folder = Folders.objects.get(name=folder_name)
    assert folder.repositories.count() >= 2

@given('folder "{folder_name}" has less than two repositories')
def step_impl(context, folder_name):
    folder = Folders.objects.get(name=folder_name)
    assert folder.repositories.count() < 2

@when('I press the "Compare" button')
def step_impl(context):
    context.browser.find_by_value('Compare').first.click()

@then('I should be redirected to "{url}"')
def step_impl(context, url):
    assert context.browser.url == url

@then('I should see a "Table of Repository Statistics Comparison"')
def step_impl(context):
    assert 'Table of Repository Statistics Comparison' in context.browser.html

@then('I should see an error message "{error_message}"')
def step_impl(context, error_message):
    assert error_message in context.browser.html

@then('I should remain on the "Add Repository" page')
def step_impl(context):
    assert 'Add Repository' in context.browser.title
