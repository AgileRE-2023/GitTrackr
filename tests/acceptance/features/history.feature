Feature: Show History of Folders
    As a logged-in user
    I want to view the history of folders containing repositories that I have created in the GitTrackr application
    So that I can revisit folders I've created.

    Scenario: Show History Successfully
        Given I am on the "http://127.0.0.1:8000/logged/"
        When I press "Hello, {username}" on the navigation bar
        And I press the "History" dropdown option
        Then the response should contain "Show History Success"
        And I should be on the "http://127.0.0.1:8000/utilities/history/"

    Scenario: Show History Unsuccessful
        Given I am on the "http://127.0.0.1:8000/logged/"
        When I press "Hello, {username}" on the navigation bar
        And I fail to press the "History" dropdown option
        Then the response should not contain "Show History Success"
        And I should stay on "http://127.0.0.1:8000/logged/"

    Scenario: Show History and Navigate to Next Folder
        Given I am on the "http://127.0.0.1:8000/logged/"
        When I press "Hello, {username}" on the navigation bar
        And I press the "History" dropdown option
        Then the response should contain "Show History Success"
        And I should be on the "http://127.0.0.1:8000/utilities/history/"
        When I press some "Folder"
        Then I should be on the "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/"
