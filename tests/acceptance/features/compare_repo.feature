Feature: Compare Repositories
    As a logged-in user
    I want to compare repositories within a folder
    So that I can analyze detailed statistical comparisons between them

    Scenario: Successfully Compare Repositories
        Given I am on TestingBDD folder page 
        And folder TestingBDD has at least two repositories added
        When I press the Compare button
        Then I should be redirected to Comparison Repositories Page

    Scenario: Failed to Compare Repositories
        Given I am on TestingBDD folder page 
        And folder TestingBDD has less than two repositories
        When I press the Compare button
        Then I should see an error message Failed to Retrieve Data from GitHub API
