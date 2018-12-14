from behave import given, when, then


@given(u'I insert my pin')
def step_insert_my_pin(context):
    print(u'STEP: Given I insert my pin')


@given(u'I have $100 in my account')
def step_money_in_my_account(context):
    print(u'STEP: Given I have $100 in my account')


@when(u'I select withdrawal')
def step_select_withdrawal(context):
    print(u'STEP: When I select withdrawal')


@when(u'I request $20')
def step_request_amount(context):
    print(u'STEP: When I request $20')


@then(u'$20 should be dispensed')
def step_dispensed_amount(context):
    print(u'STEP: Then $20 should be dispensed')


@then(u'the balance is 80$')
def step_balance_account(context):
    print(u'STEP: Then the balance is 80$')