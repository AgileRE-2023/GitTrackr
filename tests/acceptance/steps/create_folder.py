# features/steps/folder_steps.py

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from master.models import Folders
from django.test import Client

@given('I am logged in and on the page homepage GitTrackr')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    # Login using the provided test account
    context.client.login(username='testbdd@gmail.com', password='testbdd')
    
    # Navigate to the homepage
    context.browser.get('http://127.0.0.1:8000/logged/')

@when('I enter TestingBDD into the folder name field')
def step_impl(context, folder_name):
    folder_name = 'TestingBDD'
    folder_name_input = context.browser.find_element(By.XPATH, '//*[@id="id_folder_name"]').send_keys(folder_name)
    folder_name_input.send_keys(folder_name)

@when('I click the Create button')
def step_impl(context):
    # Click the Create button
    create_button = context.browser.find_element(By.ID, 'createButton')
    create_button.click()

@then('a new folder named TestingBDD should be created and saved in the database')
def step_impl(context):
    # Verify that the folder with the specified name exists in the database
    assert Folders.objects.filter(name='TestingBDD').exists()

@then('I should be redirected to the add repository page for the created folder TestingBDD')
def step_impl(context):
    # Retrieve folder_id from the database based on folder_name
    folder = Folders.objects.get(name='TestingBDD')
    folder_id = folder.id
    
    # Build the URL for the add repository page using the retrieved folder_id
    add_repository_url = f'http://127.0.0.1:8000/utilities/add_repository/{folder_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == add_repository_url

@when('I enter a duplicate folder name into the folder name field')
def step_impl(context):
    # Find the folder name input field and enter a duplicate folder name
    folder_name_input = context.browser.find_element(By.XPATH, '//*[@id="id_folder_name"]')
    folder_name_input.send_keys('TestingBDD')  # Assuming 'TestingBDD' is a duplicate name

@then('the response should contain "Folder creation failed: Duplicate name"')
def step_impl(context):
    # Assuming there is an error message element on the page
    error_message = context.browser.find_element(By.ID, 'error_message')
    assert 'Duplicate name' in error_message.text

@then('I should remain on the same page')
def step_impl(context):
    # Add validation logic to check if the browser is still on the same page
    assert context.browser.current_url == 'http://127.0.0.1:8000/logged/'
