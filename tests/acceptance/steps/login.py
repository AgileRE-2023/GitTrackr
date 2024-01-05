from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import Client
from django.contrib.auth.models import User
from time import sleep

@given('I am on the GitTrackr homepage')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:8000/')

@when('I click the Login button')
def step_impl(context):
    redirectLogin_button = context.browser.find_element(By.ID, 'redirectLoginbutton')
    redirectLogin_button.click()

@then('I should be redirected to the login page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/accounts/login/'

@when('I click sign in with google button')
def step_impl(context):
    signGoogle_button = context.browser.find_element(By.ID, 'signGoogle')
    signGoogle_button.click()

@then('I should be redirected to google oauth choose account selection')
def step_impl(context):
    assert 'accounts.google.com' in context.browser.current_url

@when('I fill the email address')
def step_impl(context):
    context.browser.find_element(By.ID, 'identifierId').send_keys('gittrackr@gmail.com')
    context.browser.find_element(By.ID, 'identifierNext').click()
    sleep(2)  # Adjust sleep time based on page load times

@when('I fill the password')
def step_impl(context):
    context.browser.find_element(By.NAME, 'password').send_keys('correct_password')
    sleep(2)  # Adjust sleep time based on page load times

@when('I fill the wrong password')
def step_impl(context):
    context.browser.find_element(By.NAME, 'password').send_keys('incorrect_password')
    sleep(2)  # Adjust sleep time based on page load times

@when('I click next')
def step_impl(context):
    context.browser.find_element(By.ID, 'passwordNext').click()
    sleep(2)  # Adjust sleep time based on page load times

@then('I should be redirected to the GitTrackr dashboard')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/logged/'

@then('I should stay on the login page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/accounts/login/'
