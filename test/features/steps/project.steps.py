from behave import given, when, then


@given(u'I create a project')
def step_impl(context):
    print(u'STEP: Given I create a project')


@when(u'I edit a project')
def step_impl(context):
    print(u'STEP: When I edit a project')


@then(u'Project is updated')
def step_impl(context):
    print(u'STEP: Then Project is updated')


@given(u'I have ${amount:d} in my account')
def step_impl(context, amount):
    print(u'STEP: Given I have %s in my account # the context' % str(amount))


@when(u'I request $20 # the event(s)')
def step_impl(context):
    print(u'STEP: When I request $20 # the event(s)')


@then(u'$20 should be dispensed # the outcome(s)')
def step_impl(context):
    print(u'STEP: Then $20 should be dispensed # the outcome(s)')


@given(u'I insert my PIN')
def step_impl(context):
    print(u'STEP: Given I insert my PIN')


# @given(u'I have $100 in my account')
# def step_impl(context):
#   print(u'STEP: Given I have $100 in my account')


@when(u'I select withdrawal')
def step_impl(context):
    print(u'STEP: When I select withdrawal')


@when(u'I request $20')
def step_impl(context):
    print(u'STEP: When I request $20')


@then(u'$20 should be dispensed')
def step_impl(context):
    print(u'STEP: Then $20 should be dispensed')


@then(u'the balance is 80$')
def step_impl(context):
    print(u'STEP: Then the balance is 80$')


@given(u'my card is invalid')
def step_impl(context):
    print(u'STEP: Given my card is invalid')


@when(u'I request $50')
def step_impl(context):
    print(u'STEP: When I request $50')


@then(u'my card should not be returned')
def step_impl(context):
    print(u'STEP: Then my card should not be returned')


@then(u'I should be told to contact the bank')
def step_impl(context):
    print(u'STEP: Then I should be told to contact the bank')


@given(u'I request $50')
def step_impl(context):
    print(u'STEP: Given I request $50')


@given(u'my card should not be returned')
def step_impl(context):
    print(u'STEP: Given my card should not be returned')


@given(u'I should be told to contact the bank')
def step_impl(context):
    print(u'STEP: Given I should be told to contact the bank')


@when(u'I choose to withdraw the fixed amount of $50')
def step_impl(context):
    print(u'STEP: When I choose to withdraw the fixed amount of $50')


@then(u'I should receive $50 cash')
def step_impl(context):
    print(u'STEP: Then I should receive $50 cash')


@then(u'the balance of my account should be $450')
def step_impl(context):
    print(u'STEP: Then the balance of my account should be $450')


@when(u'I choose to withdraw the fixed amount of $100')
def step_impl(context):
    print(u'STEP: When I choose to withdraw the fixed amount of $100')


@then(u'I should receive $100 cash')
def step_impl(context):
    print(u'STEP: Then I should receive $100 cash')


@then(u'the balance of my account should be $400')
def step_impl(context):
    print(u'STEP: Then the balance of my account should be $400')


@when(u'I choose to withdraw the fixed amount of $200')
def step_impl(context):
    print(u'STEP: When I choose to withdraw the fixed amount of $200')


@then(u'I should receive $200 cash')
def step_impl(context):
    print(u'STEP: Then I should receive $200 cash')


@then(u'the balance of my account should be $300')
def step_impl(context):
    print(u'STEP: Then the balance of my account should be $300')


@given(u'I have pushed my card in the slot')
def step_impl(context):
    print(u'STEP: Given I have pushed my card in the slot')


@when(u'I enter my PIN')
def step_impl(context):
    print(u'STEP: When I enter my PIN')


#@when(u'I press "OK"')
#def step_impl(context):
#    print(u'STEP: When I press "OK"')


@then(u'I should see the main menu')
def step_impl(context):
    print(u'STEP: Then I should see the main menu')


@given(u'I have pushed my card into the slot')
def step_impl(context):
    print(u'STEP: Given I have pushed my card into the slot')


@given(u'I have authenticated with the correct PIN')
def step_impl(context):
    context.execute_steps('''
        Given I have pushed my card in the slot
        When I enter my PIN
            And I press "OK"
    ''')


@given(u'I already registered ${amount:d}')
def step_impl(context, amount):
    print(u'STEP: Given I already registered %s' % str(amount))


@step(u'I enter my PIN ${amount:d}')
def step_impl(context, amount):
    print(u'STEP: When I enter my PIN %s' % str(amount))


@step(u'I press ${amount:d}')
def step_impl(context, amount):
    print(u'STEP: And I press "%s"' % str(amount))


@step(u'a customer {amount}')
def step_impl(context, amount):
    context.execute_steps('''
        Given I already registered %s
        When I enter my PIN %s
            And I press %s
    ''' % (amount, amount, amount))