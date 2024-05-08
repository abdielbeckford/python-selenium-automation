
Feature: Target sign in

  Scenario: User can sign in
    Given Open Target main page
    When Click Target signin button
    When Click 'Sign in' as the pop-up appears
    Then Verify your taken to 'Sign into your Target account' page