from behave import Given, When, Then, Step
#
#
# @Given(u'I have pushed my card in the slot')
# def step1(context):
#     print("step1")
#
#
# @When(u'I enter my PIN')
# def step2(context):
#     print ("step2")
#
#
# @Step(u'I press "OK"')
# def step3(context):
#     print ("step3")
#
#
# @Then(u'I should see the main menu')
# def step4(context):
#     print("step4")
#
#
# @Given(u'I have authenticated with the correct PIN')
# def step_impl(context):
#     context.ejecute_steps(u'''
#         Given I have pushed my card in the slot
#         When I enter my PIN
#         And I press "OK"
#     ''')
#
#
# # @given(u'a customer {amount}')
# # def step_impl2(context,amount):
# #     context.ejecute_steps ('''
# #         Given I have %s in my account
# #             And I have pushed my card into the slot
# #             And I enter my PIN
# #             And I press "OK"
# #         When I choose to withdraw the fixed amount of %s
# #         Then I should receive %s cash
# #             And the balance of my account should be %s
# #     ''' % (amount, amount, amount, amount))