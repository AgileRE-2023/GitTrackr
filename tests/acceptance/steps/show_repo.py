from master.models import Repository
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from master.models import Folders, Repository
from django.test import Client
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Compare Repository page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    # Login using the provided test account
    context.client.login(username='testbdd@gmail.com', password='testbdd')

    # Retrieve folder_id from the database based on folder_name
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    folder_id = folder.id
    
    # Build the URL for the compare_repo page using the retrieved folder_id
    compare_repo_url = f'http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == compare_repo_url

@when('I press the "i" button next to a repository')
def step_impl(context):
    repository_row = context.browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/table/tbody/tr')
    
    context.repository_id = repository_row.get_attribute('data-repo-id')

@then('I should be redirected to show detailed repository page')
def step_impl(context):
    # Dynamically create the URL for the detailed repository page
    detailed_page_url = f'http://127.0.0.1:8000/utilities/repository_detail/{context.repository_id}/'
    
    # Visit the detailed repository page
    context.browser.get(detailed_page_url)

@when('I press the Dropdown Button')
def step_impl(context):
    # Replace this with the actual locator for the dropdown button
    dropdown_button = context.browser.find_element(By.XPATH, '//*[@id="commitDropdown"]/button')
    dropdown_button.click()

@when('I select Another Statistic from the dropdown')
def step_impl(context):
    # Replace this with the actual locator for the dropdown options
    another_statistic_option = context.browser.find_element(By.XPATH, '//*[@id="commitDropdownMenu"]/div[2]')
    another_statistic_option.click()

@then('I should see Another Graphics Statistic')
def step_impl(context):
    # Locate the dropdown element
    dropdown = context.browser.find_element(By.XPATH, '//*[@id="selectedChartType"]')
    
    # Get the text content of the selected chart type
    selected_chart_type = dropdown.text

    # Check if the selected chart type is 'Pull Request'
    assert selected_chart_type == 'Pull Request', f"Expected 'Pull Request', but found '{selected_chart_type}'"

@then('I should not be redirected to show detailed repository page')
def step_impl(context):
    # Retrieve folder_id from the database based on folder_name
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    folder_id = folder.id
    
    # Build the URL for the compare_repo page using the retrieved folder_id
    compare_repo_url = f'http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == compare_repo_url

@then('the response status should show message "Failed to Retrieve Data from GitHub API"')
def step_impl(context):
    # Assuming there's an element containing the response status message
    context.error_message = "Failed to Retrieve Data from GitHub API"
