Feature: Create Folder
    As a logged-in user
    I want to create a new folder
    So that I can organize my repositories

    Scenario: Successfully creating a new folder
        Given I am logged in and on the page "http://127.0.0.1:8000/logged/"
        When I enter "TestingBDD" into the folder name field
        And I click the "Create" button
        Then a new folder named "TestingBDD" should be created and saved in the database
        And the response should contain "Folder successfully created"
        And I should be redirected to the add repository page for the created folder which is contain url "http://127.0.0.1:8000/utilities/add_repository/{id folder}/"

    Scenario: Failed to create a new folder due to duplicate name
        Given I am logged in and on the page "http://127.0.0.1:8000/logged/"
        When I enter a duplicate folder name into the folder name field
        And I click the "Create" button
        Then the response should contain "Folder creation failed: Duplicate name"
        And I should remain on the same page
