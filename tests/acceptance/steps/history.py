from behave import given, when, then
from master.models import Folders, Repository
from django.urls import reverse

@given('I am on the "http://127.0.0.1:8000/logged/"')
def step_impl(context):
    context.browser.visit("http://127.0.0.1:8000/logged/")

@when('I press "Hello, {username}" on the navigation bar')
def step_impl(context, username):
    hello_button = context.browser.find_by_text(f"Hello, {username}").first
    hello_button.click()

@when('I press the "History" dropdown option')
def step_impl(context):
    history_option = context.browser.find_by_text("History").first
    history_option.click()

@then('the response should contain "Show History Success"')
def step_impl(context):
    assert "Show History Success" in context.browser.html

@then('I should be on the "http://127.0.0.1:8000/utilities/history/"')
def step_impl(context):
    assert context.browser.url == "http://127.0.0.1:8000/utilities/history/"

@then('And I should stay on "http://127.0.0.1:8000/logged/"')
def step_impl(context):
    assert context.browser.url != "http://127.0.0.1:8000/logged/"

@when('I press some "Folder"')
def step_impl(context):
    folder_link = context.browser.find_by_css("a[href^='/utilities/add_repository/']").first
    folder_link.click()

@then('I should be on the "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/"')
def step_impl(context, folder_id):
    assert context.browser.url == f"http://127.0.0.1:8000/utilities/add_repository/{folder_id}/"
