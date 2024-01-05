from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from master.models import Folders, Repository
from django.test import Client

@given('folder TestingBDD has at least two repositories added')
def step_impl(context):
    # Add GitTrackr repository
    repository_name_input = context.browser.find_element(By.XPATH, '//*[@id="id_repository_name"]')
    repository_name_input.send_keys('GitTrackr')
    submit_button = context.browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/form/input[3]')
    submit_button.click()
    
    # Check if GitTrackr is added
    repository_list = context.browser.find_element(By.ID, 'repository_list')
    assert 'GitTrackr' in repository_list.text

    # Add GitTrackr to TestingBDD folder
    add_button = context.browser.find_element(By.ID, 'addRepo')
    add_button.click()

    # Add NoveltyChecker repository
    repository_name_input = context.browser.find_element(By.XPATH, '//*[@id="id_repository_name"]')
    repository_name_input.send_keys('NoveltyChecker')
    submit_button.click()

    # Check if NoveltyChecker is added
    assert 'NoveltyChecker' in repository_list.text

    # Add NoveltyChecker to TestingBDD folder
    add_button.click()

@when('I press the Compare button')
def step_impl(context):
    compare_button = context.browser.find_element(By.ID, 'compareButton')
    compare_button.click()

@then('I should be redirected to Comparison Repositories Page')
def step_impl(context):
    
    # Retrieve folder_id from the database based on folder_name
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    folder_id = folder.id
    
    # Build the URL for the add compare page using the retrieved folder_id
    compare_repo_url = f'http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == compare_repo_url

@given('folder TestingBDD has less than two repositories')
def step_impl(context):
    # Retrieve the folder based on the name 'TestingBDD'
    try:
        folder = Folders.objects.get(Folder_Name='TestingBDD')
    except Folders.DoesNotExist:
        # Handle the case where the folder doesn't exist
        context.folder_exists = False
        return

    # Check the number of repositories in the folder
    repository_count = folder.repositories.count()  # Assuming repositories is a related name in Folder model

    # Store the result in the context
    context.folder_exists = True
    context.less_than_two_repos = repository_count < 2

@then('I should see an error message Failed to Retrieve Data from GitHub API')
def step_impl(context):
    # Assuming the error message has a specific ID
    error_message = context.browser.find_element(By.ID, 'error_message')
    assert 'Failed to Retrieve Data from GitHub API' in error_message.text