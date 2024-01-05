from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from master.models import Folders, Repository
from django.test import Client

@when('I press My Username on the navigation bar')
def step_impl(context):
    # Assuming the username link has an ID like 'usernameLink'
    username_link = context.browser.find_element(By.XPATH,'/html/body/nav/div/button')
    username_link.click()

@when('I press the History dropdown option')
def step_impl(context):
    # Assuming the history dropdown option has an ID like 'historyDropdown'
    history_dropdown = context.browser.find_element(By.XPATH,'//*[@id="dropdownMenu"]/a[1]')
    history_dropdown.click()

@then('I should be on the history page')
def step_impl(context):
    # Assuming you have a unique element on the history page to verify
    assert context.browser.get('http://127.0.0.1:8000/utilities/history/')

@when('I fail to press the History dropdown option')
def step_impl(context):
    # This can be simulated by not clicking the history dropdown option
    pass

@then('I should stay on homepage')
def step_impl(context):
    # Assuming you have a unique element on the homepage to verify
    assert context.browser.get('http://127.0.0.1:8000/logged/')

@when('I press one Folder')
def step_impl(context):
    # Your implementation to click on a folder, assuming it has an ID like 'folderLink'
    folder_link = context.browser.find_element(By.XPATH,'/html/body/div[3]/div/div')
    folder_link.click()

@then('I should be on the folder page')
def step_impl(context):
    folder_name_element = context.browser.find_element(By.XPATH, '/html/body/div[3]/div/div/a/div/div[1]/h1/b')
    folder_name = folder_name_element.text

    # Query the Folders model to check if the folder exists
    folder_exists = Folders.objects.filter(name=folder_name).exists()
    assert folder_exists, f"Folder '{folder_name}' does not exist in the database."

    # Additionally, check if the current page contains the folder name
    assert folder_name in context.browser.page_source