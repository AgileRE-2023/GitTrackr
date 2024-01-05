# Filename: steps/sort_tables_steps.py
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the table is sorted in ascending order of Commit')
def step_impl(context):
    context.execute_steps(u'''
        Given I am on the Compare Repository page
        When I press the column header Commit
    ''')

@when('I press the column header Commit')
def step_impl(context):
    # Find and click the Commit column header, replace with the actual locator
    commit_column_header = context.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/table/thead/tr/th[2]/div')
    commit_column_header.click()

@when('I press the column header Commit again')
def step_impl(context):
    # Find and click the Commit column header, replace with the actual locator
    commit_column_header = context.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/table/thead/tr/th[2]/div')
    commit_column_header.click()

@then('the table should be sorted in ascending order of Commit')
def step_impl(context):
    # Implement logic to verify that the table is sorted in ascending order
    # This may involve fetching table data and comparing values
    # Placeholder logic:
    assert True, "Table is not sorted in ascending order"

@then('the table should be sorted in descending order of Commit')
def step_impl(context):
    # Implement logic to verify that the table is sorted in descending order
    # This may involve fetching table data and comparing values
    # Placeholder logic:
    assert True, "Table is not sorted in descending order"
