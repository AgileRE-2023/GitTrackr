Feature: Show Repository Details
    As a logged-in user
    I want to view detailed information about a repository, including general information, statistics, and selectable statistical graphs
    So that I can analyze and understand the repository's activities

    Scenario: Show Repository Detail Successfully
        Given I am on the "Compare Repository" page at "http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/"
        When I press the "i" button next to a repository
        Then I should be redirected to "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/"
        And I should see detailed information about the repository, including general information, statistics, and statistical charts

    Scenario: Explore Repository Detail Statistics
        Given I am on the "Compare Repository" page at "http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/"
        When I press the "i" button next to a repository
        Then I should be redirected to "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/"
        And I should see detailed information about the repository, including general information, statistics, and statistical charts
        When I press the "Dropdown Button"
        And I select "Another Statistic" from the dropdown
        Then I should see "Another Graphics Statistic"

    Scenario: Show Repository Detail Failed
        Given I am on the "Compare Repository" page at "http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/"
        When I press the "i" button next to a repository
        Then I should not see detailed information about the repository
        And the response status code should be "Failed to Retrieve Data from GitHub API"
        And I remain on the "Compare Repository" page at "http://127.0.0.1:8000/comparison/compare_repositories/{folder_id}/"
