Feature: Add Repositories
    As a logged-in user
    I want to add and remove repositories to/from the folder that I have created
    So that I can manage my repository comparisons

    Scenario: Add Repository Successfully
        Given I am on TestingBDD folder page 
        When I fill in Repository Name with GitTrackr
        And I submit the form button
        Then I should see GitTrackr in the list of repositories
        When I press Add to my folder button for GitTrackr repository
        Then the database should have GitTrackr associated with TestingBDD folder

    Scenario: Remove Added Repository
        Given GitTrackr repository is added to TestingBDD folder
        And I am on TestingBDD folder page 
        When I press X button next to GitTrackr
        Then GitTrackr should be removed from TestingBDD in the database
