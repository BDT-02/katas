# Created by Administrator at 12/13/2018
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Successful withdrawal from an account in credit
    Given I have $100 in my account
    When I request $20
    Then $20 should be dispensed

  Scenario: Successful withdrawal from an account in credit
    Given I insert my PIN
    Given I have $100 in my account
    When I select withdrawal
    When I request $20
    Then $20 should be dispensed
    Then the balance is 80$

  Scenario: Successful withdrawal from an account in credit
    Given I insert my PIN
    Then I have $100 in my account
    When I select withdrawal
    Then I request $20
    Then $20 should be dispensed
    Then the balance is 80$

  Scenario: Attempt withdrawal using stolen card
    Given I have $100 in my account
    Then my card is invalid
    When I request $50
    Then my card should not be returned
    Then I should be told to contact the bank

  Scenario: Attempt withdrawal using stolen card
    Given I have $100 in my account
    Given my card is invalid
    When I request $50
    Then my card should not be returned
    Then I should be told to contact the bank

  Scenario: Attempt withdrawal using stolen card
    * I have $100 in my account
    * my card is invalid
    * I request $50
    * my card should not be returned
    * I should be told to contact the bank
