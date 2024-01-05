Feature: Delete Repository
    As a logged-in user
    I want to delete a repository
    So that the repositories that I don't want can be deleted.

    Scenario: Success Delete Repository
        Given GitTrackr repository is added to TestingBDD folder
        And I am on TestingBDD folder page 
        When I press X button next to GitTrackr
        Then GitTrackr should be removed from TestingBDD in the database

    Scenario: Failed Delete Repository
        Given GitTrackr repository is added to TestingBDD folder
        And I am on TestingBDD folder page 
        When I press X button next to GitTrackr
        Then system displays the message Error Failed to Delete Repository
