# Created by abdie at 5/8/2024
Feature: Cart tests
  Scenario: User can add product to cart
    Given Open Target main page
    When Search for 'Mango'
    Then 'Mango' Search result is shown
    And Click add to cart
    And Click view cart & check out
    Then Verify 'Mango' is added to cart
