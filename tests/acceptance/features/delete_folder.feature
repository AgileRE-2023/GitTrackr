Feature: Delete Folder
    As a logged-in user
    I want to delete a folder
    So that I can manage folders more efficiently.

    Scenario : Delete Folder Successful
        Given I am on History Page
        When I press Hapus Folder button on one of the folders
        Then systems will delete the folder from the database
        And systems displays the alert Delete Folder Successful

    Scenario : Delete Folder Failed
        Given I am on History Page
        When I press Hapus Folder button on one of the folders
        Then system displays the message Error Failed to Delete Folder
