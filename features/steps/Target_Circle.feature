# Created by abdie at 5/7/2024
Feature: Tests for Target Circle
  Scenario: Verify user can access Target circle
    Given Open Target Circle
    Then Verify header is shown

  Scenario: Verify Target Circle page has certain amount of benefits
    Given Open Target Circle page
    Then Verify Target Circle has 10 benefit cells
