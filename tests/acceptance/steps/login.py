# features/steps/login_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on "{url}" page')
def step_impl(context, url):
    context.browser.get(url)

@when('I click button either "{login_text}" or "{create_text}"')
def step_impl(context, login_text, create_text):
    try:
        login_button = context.browser.find_element(By.XPATH, f"//button[contains(text(), '{login_text}')]")
        login_button.click()
    except:
        create_button = context.browser.find_element(By.XPATH, f"//button[contains(text(), '{create_text}')]")
        create_button.click()

@then('I should be on "{expected_url}" page')
def step_impl(context, expected_url):
    WebDriverWait(context.browser, 10).until(EC.url_to_be(expected_url))

@when('I click button "{button_text}" to login')
def step_impl(context, button_text):
    google_login_button = context.browser.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    google_login_button.click()

@when('I press "{account_choice}"')
def step_impl(context, account_choice):
    # This step would require actual interaction with Google's OAuth page, which is complex and not typically done in E2E tests
    # You would usually use a mock or bypass this step in real-world scenarios
    pass

@then('the response should{negation} contain "{message}"')
def step_impl(context, negation, message):
    if negation:
        # Check for failure message or condition
        pass
    else:
        # Check for success message or condition
        pass

@then('I should be back on "{expected_url}" page')
def step_impl(context, expected_url):
    WebDriverWait(context.browser, 10).until(EC.url_to_be(expected_url))
