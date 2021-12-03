Feature: Test the Patient creation feature

Scenario: Creation of patient account by submitting valid Patient details
  Given I navigate to the url
  When I enter the patient's First name
  When I enter the patient's Middle name
  When I enter the patient's Last name
  When I enter the patient's Phone number
  When I enter the patient's Date of Birth
  When I enter the patient's Address
  And I click on the Add New User button
  Then A patient account should be created with the details provided.