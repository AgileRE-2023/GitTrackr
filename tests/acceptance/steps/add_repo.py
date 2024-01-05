from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from master.models import Folders, Repository
from django.test import Client

@given('I am on TestingBDD folder page')
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

@when('I fill in Repository Name with GitTrackr')
def step_impl(context):
    # Find the Repository Name input field and enter the repository name
    repository_name_input = context.browser.find_element(By.XPATH, '//*[@id="id_repository_name"]').send_keys('GitTrackr')

@when('I submit the form button')
def step_impl(context):
    # Submit the form
    submit_button = context.browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/form/input[3]')
    submit_button.click()

@then('I should see GitTrackr in the list of repositories')
def step_impl(context):
    # Assuming there is a list of repositories on the page
    repository_list = context.browser.find_element(By.ID, 'repository_list')
    assert 'GitTrackr' in repository_list.text

@when('I press Add to my folder button for GitTrackr repository')
def step_impl(context):
    # Assuming there is a button to add the repository to the folder
    add_button = context.browser.find_element(By.ID, 'addRepo')
    add_button.click()

@then('the database should have GitTrackr associated with TestingBDD folder')
def step_impl(context):
    # Verify that GitTrackr is associated with the TestingBDD folder in the database
    folder = Folders.objects.get(Folder_Name='TestingBDD')
    repository = Repository.objects.get(Repository_Name='GitTrackr', folder=folder)
    assert repository is not None

@given('GitTrackr repository is added to TestingBDD folder')
def step_impl(context):
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
