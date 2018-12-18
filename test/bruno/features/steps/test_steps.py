from behave import given, when, then
from compare import expect


@given(u'I insert my PIN')
def step_impl(context):
    print(u'STEP: Given I insert my PIN')


@given(u'I have $100 in my account')
def step_impl(context):
    print(u'STEP: Given I have $100 in my account')


@when(u'I select withdrawal')
def step_impl(context):
    print(u'STEP: When I select withdrawal')
    context.saldo = 100


@when(u'I request ${amount:d}')
def step_impl(context, amount):
    print(u'STEP: When I request $%s' % amount)
    context.saldo = context.saldo - amount
    context.dsispensed = amount

@then(u'${amount:d} should be dispensed')
def step_impl(context, amount):
    print(u'STEP: Then $%s should be dispensed' % amount)
    assert context.dsispensed == amount
    expect(context.dsispensed).to_equal(amount)

@then(u'the balance is {amount:d}$')
def step_impl(context, amount):
    print(u'STEP: Then the balance is %s$' % amount)
    assert context.saldo == amount, 'the balance is %s$' % amount


