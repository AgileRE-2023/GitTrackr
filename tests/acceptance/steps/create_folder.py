from behave import given, when, then
from master.models import Folders
from django.urls import reverse
from django.shortcuts import resolve_url
from django.core.exceptions import ObjectDoesNotExist
from django.test import Client

@given('I am logged in and on the page "{page_url}"')
def step_impl(context, page_url):
    # Suppose you have a login mechanism, implement it here
    context.response = context.client.get(context.get_url(page_url))

@when('I enter "{folder_name}" into the folder name field')
def step_impl(context, folder_name):
    context.folder_name = folder_name

@when('I click the "Create" button')
def step_impl(context):
    response = context.client.post(reverse('create_folder'), {'folder_name': context.folder_name})
    context.response = response

@then('a new folder named "{expected_folder_name}" should be created and saved in the database')
def step_impl(context, expected_folder_name):
    try:
        folder = Folders.objects.get(Folder_Name=expected_folder_name)
        assert folder is not None, f'Folder with name {expected_folder_name} not found in the database.'
    except ObjectDoesNotExist:
        assert False, f'Folder with name {expected_folder_name} not found in the database.'

@then('the response should contain "{expected_response}"')
def step_impl(context, expected_response):
    assert expected_response in context.response.content.decode(), f'Response does not contain expected text: {expected_response}'

@then('I should be redirected to the add repository page for the created folder which is contain url "{expected_url}"')
def step_impl(context, expected_url):
    folder = Folders.objects.latest('Created_At')
    expected_url = reverse('add_repository_with_folder', kwargs={'folder_id': folder.id})
    assert context.response.url == context.get_url(expected_url), f'Expected URL: {expected_url}, Actual URL: {context.response.url}'

@then('I should remain on the same page')
def step_impl(context):
    assert context.response.url == context.get_url(reverse('logged')), 'Expected to remain on the same page, but redirected.'
