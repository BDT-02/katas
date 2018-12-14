from behave import Given, Step


@Given(u'a User "Michael Jackson" born on August 29, 1958')
def step1(context):
    print("|Michael Jackson| August 29, 1958|")
    print('')


@Step(u'a User "Elvis" born on January 8, 1935')
def step2(context):
    print("|Elvis| January 8, 1935|")
    print('')


@Step(u'a User "John Lennon" born on October 9, 1940')
def step3(context):
    print("|John Lennon| October 9, 1940|")
    print('')

