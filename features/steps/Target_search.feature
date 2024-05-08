# Created by abdie at 5/7/2024
Feature:  Search Tests

  Scenario: User can search for coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown


  Scenario Outline: User can search for an item
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    And Verify <expected_item> in search result url
    Examples:
    |item        |expected_item    |
    |coffee      |coffee           |
    |tea         |tea              |
    |mug         |mug              |