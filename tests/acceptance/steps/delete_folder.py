# features/steps/folder_steps.py

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from master.models import Folders
from django.test import Client

@given('I am on History Page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    # Login using the provided test account
    context.client.login(username='testbdd@gmail.com', password='testbdd')
    
    # Navigate to the homepage
    context.browser.get("http://127.0.0.1:8000/history")

# Step for "When I press Hapus Folder button on one of the folders"
@when('I press Hapus Folder button on one of the folders')
def step_impl(context):
    deleteFolder_button = context.browser.find_element(By.XPATH,'/html/body/div[3]/div/div/form/button')
    deleteFolder_button.click()

# Step for "Then systems will delete the folder from the database"
@then('systems will delete the folder from the database')
def step_impl(context):
    folder_deleted = not Folders.objects.filter(name=context.folder_name).exists()  # Assumes Django ORM
    assert folder_deleted, f"Folder '{context.folder_name}' should be deleted from the database"

# Step for "And systems displays the alert Delete Folder Successful"
@then('systems displays the alert Delete Folder Successful')
def step_impl(context):
    # Assuming the alert is a simple popup or JavaScript alert
    alert = context.browser.switch_to.alert
    assert "Delete Folder Successful" in alert.text
    alert.accept()

# Step for "Then system displays the message Error Failed to Delete Folder"
@then('system displays the message Error Failed to Delete Folder')
def step_impl(context):
    # Assuming the error is a simple popup or JavaScript alert
    alert = context.browser.switch_to.alert
    assert "Error Failed to Delete Folder" in alert.text
    alert.accept()
