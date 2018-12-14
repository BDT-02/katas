from behave import Given, When, Then


@Given(u'I have ${amount:d} in my account')
def step1(context, amount):
    print("step1")


@When(u'I request ${amount:d}')
def step2(context, amount):
    print("step2")


@Then(u'${dispensed:d} should be dispensed')
def step3(context, dispensed):
    print("step3")


@Given("I insert my PIN")
def step4(context):
    print("step4")


@Given(u'I have ${amount:d} in my account')
def step5(context, amount):
    print("step5")


@When(u'I select withdrawal')
def step6(context):
    print("step6")


@When('I request ${dispensed:d}')
def step7(context,dispensed):
    print("step7")


@Then(u'${dispensed:d} should be dispensed')
def step8(context, dispensed):
    print("step8")


@Then(u'the balance is ${amount:d}')
def step9(context, amount):
    print("step9")


@Then(u'my card is invalid')
def step10(context):
    print("step10")


@When(u'I request ${amount:d}')
def step11(context,amount):
    print("step11")


@Then(u'my card should not be returned')
def step12(context):
    print("step12")


@Then(u'I should be told to contact the bank')
def step13(context):
    print("step13")


@Given(u'my card is invalid')
def step14(context):
    print("step14")






