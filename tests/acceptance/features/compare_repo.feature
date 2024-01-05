Feature: Compare Repositories
    As a logged-in user
    I want to compare repositories within a folder
    So that I can analyze detailed statistical comparisons between them

    Scenario: Successfully Compare Repositories
        Given I am on "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/" page for folder "TestingBDD"
        And folder "TestingBDD" has at least two repositories added
        When I press the "Compare" button
        Then I should be redirected to "http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/"
        And I should see a "Table of Repository Statistics Comparison"

    Scenario: Failed to Compare Repositories
        Given I am on "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/" page for folder "TestingBDD"
        And folder "TestingBDD" has less than two repositories
        When I press the "Compare" button
        Then I should see an error message "Failed to Retrieve Data from GitHub API"
        And I should remain on the "Add Repository" page
