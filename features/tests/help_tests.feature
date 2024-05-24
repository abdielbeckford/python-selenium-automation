Feature: Tests for Help pages

  Scenario: User can select Help topic
    Given Open Help page for returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help About Target Circle page opened