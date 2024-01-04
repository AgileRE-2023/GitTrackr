from behave import given, when, then
from master.models import Repository

@given('I am on the "Compare Repository" page at "{url}"')
def step_impl(context, url):
    context.browser.visit(url)

@when('I press the "i" button next to a repository')
def step_impl(context):
    # Assume there is a button with id "repo-details-button" for repository details
    context.browser.find_by_id('repo-details-button').first.click()

@when('I press the "Dropdown Button"')
def step_impl(context):
    # Assume there is a button with id "dropdown-button" for dropdown
    context.browser.find_by_id('dropdown-button').first.click()

@when('I select "{statistic}" from the dropdown')
def step_impl(context, statistic):
    # Assume there is a button with class "dropdown-item" for each dropdown item
    context.browser.find_by_text(statistic).first.click()

@then('I should be redirected to "{url}"')
def step_impl(context, url):
    assert context.browser.url == url

@then('I should see detailed information about the repository, including general information, statistics, and statistical charts')
def step_impl(context):
    assert 'Detail Information about The Repository' in context.browser.html

@then('I should see "{statistic}"')
def step_impl(context, statistic):
    assert statistic in context.browser.html

@then('I should not see detailed information about the repository')
def step_impl(context):
    assert 'Detail Information about The Repository' not in context.browser.html

@then('the response status code should be "{status_code}"')
def step_impl(context, status_code):
    assert context.browser.status_code == int(status_code)

@then('I remain on the "Compare Repository" page at "{url}"')
def step_impl(context, url):
    assert context.browser.url == url
