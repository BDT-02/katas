from behave import given, when, then


@given(u'I have ${Balance} in my account')
def step_account_actual_balance(context, balance):
    context.balance = balance
    print(u'STEP: Given I have <Balance> in my account')


@when(u'I choose to withdraw the fixed amount of ${Withdrawal}')
def step_choose_withdraw_amount(context, withdrawal):
    context.withdrawal = withdrawal
    print(u'STEP: When I choose to withdraw the fixed amount of <Withdrawal>')


@then(u'I should receive ${Received} cash')
def step_receive_cash(context, received):
    context.received = received
    print(u'STEP: Then I should receive <Received> cash')


@then(u'the balance of my account should be ${Remaining}')
def step_receive_cash(context, remaining):
    context.remaining = remaining
    print(u'STEP: Then The balance of my account should be <Remaining>')


