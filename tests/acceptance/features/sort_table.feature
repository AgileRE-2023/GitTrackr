Feature: Sort Tables
    As a logged-in user
    I want to sort the contents of a table column in ascending or descending order by clicking the column header
    So that it is easier for me to view and analyze the statistical comparisons.

    Scenario: Sort Table in Ascending Order
        Given I am on the Compare Repository page
        When I press the column header Commit
        Then the table should be sorted in ascending order of Commit

    Scenario: Sort Table in Descending Order
        Given the table is sorted in ascending order of Commit
        When I press the column header Commit again
        Then the table should be sorted in descending order of Commit
