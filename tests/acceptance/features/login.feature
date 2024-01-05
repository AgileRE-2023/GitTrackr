Feature: Login using Google Account
    As a guest
    I want to login to GitTrackr using my Google Account
    So that I can securely access and use GitTrackr features

    Scenario: Successfully logging in using GitTrackr Account
        Given I am on the GitTrackr homepage
        When I click the Login button
        Then I should be redirected to the login page
        When I click sign in with google button
        Then I should be redirected to google oauth choose account selection
        When I fill the email address
        And I fill the password
        And I click next
        Then I should be redirected to the GitTrackr dashboard

    Scenario: Failed login attempt using GitTrackr Account
        Given I am on the GitTrackr homepage
        When I click the Login button
        Then I should be redirected to the login page
        When I click sign in with google button
        Then I should be redirected to google oauth choose account selection
        When I fill the email address
        And I fill the wrong password
        And I click next
        Then I should stay on the login page
