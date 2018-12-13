# Created by Administrator at 12/13/2018
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Successful withdrawal from an account in credit
    Given I have $100 in my account
    When I request $20 # the event(s)
    Then $20 should be dispensed # the outcome(s)


  Scenario: Successful withdrawal from an account in credit
    Given I insert my PIN
    Given I have $100 in my account
    When I select withdrawal
    When I request $20
    Then $20 should be dispensed
    Then the balance is 80$


  Scenario: Successful withdrawal from an account in credit
    Given I insert my PIN
    And I have $100 in my account
    When I select withdrawal
    And I request $20
    Then $20 should be dispensed
    And the balance is 80$


  Scenario: Attempt withdrawal using stolen card
    Given I have $700 in my account
    But my card is invalid
    When I request $50
    Then my card should not be returned
    And I should be told to contact the bank


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


    # This feature covers the account transaction and hardware-driver modules
#Feature: Withdraw Cash
#In order to buy beer
#As an account holder
#I want to withdraw cash from the ATM
# Can't figure out how to integrate with magic wand interface
  #Scenario: Withdraw too much from an account in credit
    #Given I have $50 in my account
    # When I wave my magic wand
    #And I withdraw $100
    #Then I should receive $100


