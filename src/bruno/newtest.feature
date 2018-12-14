Feature: this is the behave class

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
    Given I have $100 in my account
	  But my card is invalid
    When I request $50
    Then my card should not be returned
	  And I should be told to contact the bank