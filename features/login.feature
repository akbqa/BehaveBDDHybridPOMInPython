Feature: Login Functionality

  @login
  Scenario: Login with valid credentials
    Given I navigate to login page
    When I enter valid email and valid password
    And I click on login button
    Then I should get logged in

  @login @invalid
  Scenario: Login with invalid email and valid password
    Given I navigate to login page
    When I enter invalid email and valid password into the fields
    And I click on login button
    Then I should get a proper warning message