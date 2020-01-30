@search
Feature: Shopping

  @wip
  Scenario: Check cart is empty
    Given a customer navigates to the homepage
    When they check their shopping cart
    Then the shopping cart is empty

