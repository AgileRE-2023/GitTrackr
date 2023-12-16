from behave import given, when, then
# from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

@given('I am on the landing page as a logged-in user')
def step_impl(context):
    context.client = Client()

    user = User.objects.create_user('testuser', 'test@example.com', 'password')
    context.client.force_login(user)
    context.user = user

@when('I enter "{folder_name}" into the folder name field')
def step_impl(context, folder_name):
    context.folder_name = folder_name

@when('I click the "Create" button')
def step_impl(context):
    response = context.client.post(reverse('create_folder'), {'folder_name': context.folder_name})
    context.response = response

@then('a new folder is created and saved in the database')
def step_impl(context):
    assert Folders.objects.filter(Folder_Name=context.folder_name, UserID=context.user).exists()

@then('I am redirected to the add repository page')
def step_impl(context):
    assert context.response.url == reverse('add_repository')