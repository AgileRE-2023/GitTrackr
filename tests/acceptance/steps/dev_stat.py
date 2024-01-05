# Filename: steps/show_developer_statistics_steps.py
from behave import *
from selenium.webdriver.common.by import By
from master.models import Repository
from django.test import Client
from selenium import webdriver

@given('I am on the show detailed repository page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    # Login using the provided test account
    context.client.login(username='testbdd@gmail.com', password='testbdd')

    # Retrieve repository_id from the database based on repository_name
    repository = Repository.objects.get(repository_Name='GitTrackr')
    repository_id = repository.id
    
    # Build the URL for the compare_repo page using the retrieved repository_id
    compare_repo_url = f'http://127.0.0.1:8000/utilities/repository_detail/{repository_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == compare_repo_url

@when('I press the Developer Activity button')
def step_impl(context):
    # Find and click the Developer Activity button, replace this with the actual locator
    developer_activity_button = context.browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/a/div')
    developer_activity_button.click()

@then('I should be redirected to the developer statistic page')
def step_impl(context):
    # Retrieve repository_id from the database based on repository_name
    repository = Repository.objects.get(repository_Name='GitTrackr')
    repository_id = repository.id
    # Check if the browser is redirected to the expected URL for the developer statistic page
    expected_url = f'http://127.0.0.1:8000/comparison/developer_statistic/{repository_id}/'  # Replace with the actual URL
    assert context.browser.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {context.browser.current_url}"

@then('the response status code should be "Failed to Retrieve Data from GitHub API"')
def step_impl(context):
    # Assuming there's an element containing the response status message
    context.error_message = "Failed to Retrieve Data from GitHub API"

@then('I should still be on the show detailed repository page')
def step_impl(context):
    # Retrieve repository_id from the database based on repository_name
    repository = Repository.objects.get(repository_Name='GitTrackr')
    repository_id = repository.id
    
    # Build the URL for the compare_repo page using the retrieved repository_id
    compare_repo_url = f'http://127.0.0.1:8000/utilities/repository_detail/{repository_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == compare_repo_url
