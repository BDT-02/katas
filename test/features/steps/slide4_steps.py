from behave import given, when, then


@given(u'Successful login with PIN')
def step_impl(context):
    context.execute_steps('''
        Given I have pushed my card in the slot
        When I enter my PIN
        Then I press "OK"
        Then I should see the main menu''')


@given(u'I have pushed my card in the slot')
def step_push_card(context):
    print (u'STEP: Given I have pushed my card in the slot')


@when(u'I enter my PIN')
def step_enter_pin(context):
    print (u'STEP: When I enter my PIN')


@then(u'I press "OK"')
def step_press_ok(context):
    print (u'STEP: Then I press "OK"')


@then(u'I should see the main menu')
def step_main_menu(context):
    print (u'STEP: Then I should see the menu')


@given(u'A customer {amount}')
def step_impl(context, amount):
    context.execute_steps('''
        Given I have $500 in my account
        And I have pushed my card into the slot
        And I enter my PIN
        And I press OK
        When I choose to withdraw the fixed amount of $50
        Then I should receive $50 cash
        And the balance of my account should be $450''')


@given(u'I have $500 in my account')
def step_account_balance(context):
    print(u'STEP: Given I have $500 in my account')


@then(u'I have pushed my card into the slot')
def step_pushed_card(context):
    print(u'STEP: Then I have pushed my card into the slot')


@then(u'I enter my PIN')
def step_enter_pins(context):
    print(u'STEP: Then I enter my PIN')


@then(u'I press OK')
def step_pressing_ok(context):
    print(u'STEP: Then I press OK')


@when(u'I choose to withdraw the fixed amount of $50')
def step_withdraw_money(context):
    print(u'STEP: When I choose to withdraw the fixed amount of $50')


@then(u'I should receive $50 cash')
def step_received_cash(context):
    print(u'STEP: Then I should receive $50 cash')


@then(u'The balance of my account should be $450')
def step_new_balance_account(context):
    print(u'STEP: Then the balance of my account should be $450')


@given(u'I have pushed my card into the slot')
def step_impl(context):
    print(u'STEP: Given I have pushed my card into the slot')


@given(u'I enter my PIN')
def step_impl(context):
    print(u'STEP: Given I enter my PIN')


@given(u'I press OK')
def step_impl(context):
    print(u'STEP: Given I press OK')