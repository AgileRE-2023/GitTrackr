Feature: Sort Tables
    As a logged-in user
    I want to sort the contents of a table column in ascending or descending order by clicking the column header
    So that it is easier for me to view and analyze the statistical comparisons.

    Scenario: Sort Table in Ascending Order
        Given I am on a page with a sortable table, either "http://127.0.0.1:8000/utilities/add_repository/{folder_id}/" or "http://127.0.0.1:8000/utilities/repository_detail/{repo_id}/"
        When I press the column header "Column Name"
        Then the table should be sorted in ascending order of "Column Name"

    Scenario: Sort Table in Descending Order
        Given the table is sorted in ascending order of "Column Name"
        When I press the column header "Column Name" again
        Then the table should be sorted in descending order of "Column Name"
