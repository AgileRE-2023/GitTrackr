from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from master.models import Folders, Repository
from django.test import Client

@given('GitTrackr repository is added to TestingBDD folder')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    # Login using the provided test account
    context.client.login(username='testbdd@gmail.com', password='testbdd')

    # Retrieve folder_id from the database based on folder_name
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    folder_id = folder.id
    
    # Build the URL for the add repository page using the retrieved folder_id
    add_repository_url = f'http://127.0.0.1:8000/utilities/add_repository/{folder_id}/'
    
    # Check if the browser is redirected to the correct URL
    assert context.browser.current_url == add_repository_url
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    repository = Repository.objects.create(Repository_Name='GitTrackr', folder=folder)

@when('I press X button next to GitTrackr')
def step_impl(context):
    # Assuming there is a delete button next to the repository in the list
    delete_button = context.browser.find_element(By.XPATH, '//*[@id="repositoryContainer"]/div/form/button')
    delete_button.click()

@then('GitTrackr should be removed from TestingBDD in the database')
def step_impl(context):
    # Verify that GitTrackr is removed from the TestingBDD folder in the database
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    assert not Repository.objects.filter(Repository_Name='GitTrackr', folder=folder).exists()

@then('system displays the message Error Failed to Delete Repository')
def step_impl(context):
    # Wait for the alert to be present
    WebDriverWait(context.browser, 10).until(EC.alert_is_present())

    # Switch to the alert
    alert = context.browser.switch_to.alert

    # Verify the alert text
    assert "Error Failed to Delete Repository" in alert.text

    # Accept the alert to close it
    alert.accept()
