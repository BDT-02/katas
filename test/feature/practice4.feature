Feature: practice 4 examples

#  Scenario: Successful login with PIN
#    Given I have pushed my card in the slot
#    When I enter my PIN 4834267
#    And I press "OK"
#    Then I should see the main menu
#
#  Scenario: test nested steps
#    Given I have authenticate with correct pin 4834267
#    Then I should see the main menu

#  Scenario Outline: test nested steps
#    Given I have authenticate with correct pin <pin>
#    Then I should see the main menu
#
#    Examples:
#      | pin        |
#      | 4834267    |
#      | 1234567    |
#      | 1234567789 |

#  Scenario: task about data tables
#    Given I fill the data users
#      | name | firstName | lastName | age |
#      | yury | ortuno    | calvo    | 25  |
#    When I enter create user
#    Then The user created

  Scenario: task about data tables
    Given I fill the data users
      | user  | password |
      | admin | admin123 |
    When I enter create user
    Then The user created