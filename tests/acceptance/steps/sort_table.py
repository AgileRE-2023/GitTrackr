from behave import given, when, then
from master.models import Folders, Repository
from django.urls import reverse

@given('I am on a page with a sortable table, either "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/" or "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/"')
def step_impl(context, folder_id=None, repo_id=None):
    if folder_id:
        url = reverse('add_repository', args=[folder_id])
    elif repo_id:
        url = reverse('repository_detail', args=[repo_id])
    else:
        # Define the default URL or raise an error
        pass

    context.browser.visit(f'http://127.0.0.1:8000/{url}')

@when('I press the column header "{column_name}"')
def step_impl(context, column_name):
    # Assuming you have a sortable table with header data-sort attribute
    header = context.browser.find_by_css(f'th[data-sort="{column_name}"]').first
    header.click()

@then('the table should be sorted in ascending order of "{column_name}"')
def step_impl(context, column_name):
    # Get the sorted values from the table and check if they are in ascending order
    sorted_values = get_column_values(context, column_name)
    assert sorted_values == sorted(sorted_values), f'Table is not sorted in ascending order for {column_name}'

@then('the table should be sorted in descending order of "{column_name}"')
def step_impl(context, column_name):
    # Get the sorted values from the table and check if they are in descending order
    sorted_values = get_column_values(context, column_name)
    assert sorted_values == sorted(sorted_values, reverse=True), f'Table is not sorted in descending order for {column_name}'

def get_column_values(context, column_name):
    # You need to implement this function to get the values of the specified column from the table
    # Return the values as a list
    pass
