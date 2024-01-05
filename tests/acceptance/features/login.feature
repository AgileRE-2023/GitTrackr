Feature: Login using Google Account
    As a guest
    I want to login to GitTrackr using my Google Account
    So that I can securely access and use GitTrackr features

    Scenario: Successfully logging in using Google Account
        Given I am on the GitTrackr homepage at "http://127.0.0.1:8000/"
        When I click the "Login" or "Create" button
        Then I should be redirected to the login page at "http://127.0.0.1:8000/accounts/login/"
        When I click the "Sign In with Google Account" button
        Then I should be redirected to the Google account selection page
        When I select and confirm my Google account
        Then I should receive a success response indicating successful login
        And I should be redirected to the GitTrackr dashboard at "http://127.0.0.1:8000/logged/"

    Scenario: Failed login attempt using Google Account
        Given I am on the GitTrackr homepage at "http://127.0.0.1:8000/"
        When I click the "Login" or "Create" button
        Then I should be redirected to the login page at "http://127.0.0.1:8000/accounts/login/"
        When I click the "Sign In with Google Account" button
        Then I should be redirected to the Google account selection page
        When I select and confirm my Google account
        Then I should receive an error response indicating failed login
        And I should be redirected back to the login page at "http://127.0.0.1:8000/accounts/login/"
