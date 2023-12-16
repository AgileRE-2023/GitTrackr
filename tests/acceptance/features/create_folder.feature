Feature: Create Folder
    As a logged-in user
    I want to create a new folder
    So that I can organize my repositories

    Scenario: Successfully creating a new folder
        Given I am on the landing page as a logged-in user
        When I enter "My New Folder" into the folder name field
        And I click the "Create" button
        Then a new folder is created and saved in the database
        And I am redirected to the add repository page