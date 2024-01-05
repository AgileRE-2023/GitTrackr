Feature: Show History of Folders
    As a logged-in user
    I want to view the history of folders containing repositories that I have created in the GitTrackr application
    So that I can revisit folders I've created.

    Scenario: Show History Successfully
        Given I am logged in and on the page homepage GitTrackr
        When I press My Username on the navigation bar
        And I press the History dropdown option
        Then I should be on the history page

    Scenario: Show History Unsuccessful
        Given I am logged in and on the page homepage GitTrackr
        When I press My Username on the navigation bar
        And I fail to press the History dropdown option
        Then I should stay on homepage

    Scenario: Show History and Navigate to Next Folder
        Given I am logged in and on the page homepage GitTrackr
        When I press My Username on the navigation bar
        And I press the History dropdown option
        Then I should be on the history page
        When I press one Folder
        Then I should be on the folder page
