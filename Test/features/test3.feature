# Created by Administrator at 12/14/2018
Feature: #Enter feature name here
  # Enter feature description here

  Scenario Outline: Withdraw fixed amount
    Given I have <Balance> in my account
    When I choose to withdraw the fixed amount of <Withdrawal>
    Then I should receive <Received> cash
    And the balance of my account should be <Remaining>