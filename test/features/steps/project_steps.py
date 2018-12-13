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


@given(u'I have $100 in my account # the context')
def step_impl(context):
    print(u'STEP: Given I have $100 in my account # the context')


@when(u'I request $20 # the event(s)')
def step_impl(context):
    print(u'STEP: When I request $20 # the event(s)')


@then(u'$20 should be dispensed # the outcome(s)')
def step_impl(context):
    print(u'STEP: Then $20 should be dispensed # the outcome(s)')


@given(u'I insert my PIN')
def step_impl(context):
    print(u'STEP: Given I insert my PIN')


@given(u'I have ${amount:d} in my account')
def step_impl(context,amount):
    print(u'STEP: Given I have %s in my account' % str(amount))


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
