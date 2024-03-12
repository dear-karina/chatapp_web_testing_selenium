Feature: login on chrome

  Background:
    Given I open the chrome browser

  Scenario Outline: Login with correct credentials
    Given I open the login page
    When I enter the correct username "hongducdev" and password "123456"
    Then I should be logged in successfully
  Scenario: Login with incorrect password
    Given I open the login page
    When I enter the correct username "hongducdev" and incorrect password "incorrectpassword"
    Then I should not be logged in

  Scenario: Login with nonexistent username
    Given I open the login page
    When I enter a nonexistent username "nonexistentusername" and password "123456"
    Then I should not be logged in
