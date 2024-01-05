Feature: Show Developer Statistics
    As a logged-in user
    I want to see the statistics of developers who contribute to a selected repository
    So that I can understand the contributions and activities of developers in that repository.

    Scenario: Show Developer Statistic Successfully
        Given I am on "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/" page
        When I press "Developer Activity" button in the repository detail
        Then the response should contain "Show Developer Statistic Success"
        And I should be redirected to "http://127.0.0.1:8000/comparison/developer_statistic/{repo_id}/" page
        And I should see "Comparison Table of Developer Statistics"

    Scenario: Show Developer Statistic Failed
        Given I am on "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/" page
        When I press "Developer Activity" button in the repository detail
        Then the response should not contain "Show Success"
        And the response status code should be "Failed to Retrieve Data from GitHub API"
        And I should still be on "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/" page
