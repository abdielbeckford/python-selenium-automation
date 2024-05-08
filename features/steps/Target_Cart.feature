Feature: Target cart empty

  Scenario: 'Your cart is empty' message displayed
    Given Open Target main page
    When Click on cart icon
    Then Verify cart is empty