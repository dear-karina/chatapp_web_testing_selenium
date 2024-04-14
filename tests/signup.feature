Feature: signup on chrome

  Background:
    Given I open the chrome browser

  @positive-case, @must-passed, @signup
  Scenario: Signup with valid credentials
    Given I open the signup page
    When I enter an unique fullname and an unique username and an unique password and retype it correctly
    Then I should be signed up successfully

  @negative-case, @must-passed, @signup
  Scenario: Signup with mismatching password
    Given I open the signup page
    When I enter an unique fullname and an unique username and an unique password and retype it incorrectly
    Then I should not be signed up
    And I should see the signup message "Passwords do not match"

  @negative-case, @signup
  Scenario: Signup with existed username
    Given I open the signup page
    When I enter an unique fullname and an existed username and an unique password and retype it correctly
    Then I should not be signed up
    And I should see the signup message "Username already exists"
