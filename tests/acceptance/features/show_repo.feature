Feature: Show Repository Details
    As a logged-in user
    I want to view detailed information about a repository, including general information, statistics, and selectable statistical graphs
    So that I can analyze and understand the repository's activities

    Scenario: Show Repository Detail Successfully
        Given I am on the Compare Repository page
        When I press the "i" button next to a repository
        Then I should be redirected to show detailed repository page

    Scenario: Explore Repository Detail Statistics
        Given I am on the Compare Repository page
        When I press the "i" button next to a repository
        Then I should be redirected to show detailed repository page
        When I press the Dropdown Button
        And I select Another Statistic from the dropdown
        Then I should see Another Graphics Statistic

    Scenario: Show Repository Detail Failed
        Given I am on the Compare Repository page
        When I press the "i" button next to a repository
        Then I should not be redirected to show detailed repository page
        And the response status should show message "Failed to Retrieve Data from GitHub API"
