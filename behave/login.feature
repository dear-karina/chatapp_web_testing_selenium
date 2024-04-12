Feature: Login

  Background:
    Given I open the "Log In" Page

  @login
  Scenario: Login is successful when using a valid credential
    Then All of the UI elements should align with the Login Page design
    When I enter the username "tester001" (already registered)
    When I enter the password "@K;ChV7q" (matched)
    Then I should be logged in successfully

  @login
  Scenario: Login is failed when using an invalid username
    When I enter the username "tester001" (already registered)
    When I enter the password "@K;ChV7q " (not matched)
    Then I should not be logged in
    And I should see the message "Incorrect password"

  @login
  Scenario: Login is failed when using an invalid username
    When I enter the username "tester000" (not yet registered)
    When I enter the password "@K;ChV7q" (matched)
    Then I should not be logged in
    And I should see the message "Nonexistent username"
