Feature: Add Repositories
    As a logged-in user
    I want to add and remove repositories to/from the folder that I have created
    So that I can manage my repository comparisons

    Scenario: Add Repository Successfully
        Given I am on "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/" page for folder "TestingBDD"
        When I fill in "Repository Name" with "GitTrackr" and submit the form
        Then I should be redirected to "http://127.0.0.1:8000/utilities/search_repository/"
        And I should see "GitTrackr" in the list of repositories
        When I press "Add to my folder" button for "GitTrackr"
        Then the database should have "GitTrackr" associated with "TestingBDD"
        And I should see "Add Repository Success" message

    Scenario: Remove Added Repository
        Given "GitTrackr" repository is added to "TestingBDD" folder
        And I am on the folder page for "TestingBDD"
        When I press "X" button next to "GitTrackr"
        Then "GitTrackr" should be removed from "TestingBDD" in the database
        And I should see "Deleted Repository Success" message

    Scenario: Add Repository Failed (Not Valid)
        Given I am on "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/" page for folder "TestingBDD"
        When I fill in "Repository Name" with "InvalidRepositoryName!"
        And I press "Add to my folder" button
        Then the response should contain "Add Repository Failed"
        And the "List Repository" field should not contain "GitTrackr"
