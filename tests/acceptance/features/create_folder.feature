Feature: Create Folder
    As a logged-in user
    I want to create a new folder
    So that I can organize my repositories

    Scenario: Successfully creating a new folder
        Given I am logged in and on the page homepage GitTrackr
        When I enter TestingBDD into the folder name field
        And I click the Create button
        Then a new folder named TestingBDD should be created and saved in the database
        And I should be redirected to the add repository page for the created folder TestingBDD

    Scenario: Failed to create a new folder due to duplicate name
        Given I am logged in and on the page homepage GitTrackr
        When I enter a duplicate folder name into the folder name field
        And I click the Create button
        Then the response should contain "Folder creation failed: Duplicate name"
        And I should remain on the same page
