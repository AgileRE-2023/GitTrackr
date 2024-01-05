Feature: Show Developer Statistics
    As a logged-in user
    I want to see the statistics of developers who contribute to a selected repository
    So that I can understand the contributions and activities of developers in that repository.

    Scenario: Show Developer Statistic Successfully
        Given I am on the show detailed repository page
        When I press the Developer Activity button
        Then I should be redirected to the developer statistic page

    Scenario: Show Developer Statistic Failed
        Given I am on the show detailed repository page
        When I press the Developer Activity button
        Then the response status code should be "Failed to Retrieve Data from GitHub API"
        And I should still be on the show detailed repository page