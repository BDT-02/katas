# Created by Administrator at 12/14/2018
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Successful login with PIN
    Given I have authenticated with the correct PIN
    Then I should see the main menu

#  Scenario: Withdraw fixed amount of $50
#    Given I have $500 in my account
#    And I have pushed my card into the slot
#    And I enter my PIN
#    And I press "OK"
#    When I choose to withdraw the fixed amount of $50
#    Then I should receive $50 cash
#    And the balance of my account should be $450