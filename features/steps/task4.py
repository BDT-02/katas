from behave import *

from src.utils.LoggerHandler import LoggerHandler
from src.utils.config_handler import ConfigHandler

logger = LoggerHandler.get_instance()
@given("I have pushed my card in the slot")
def step_impl1(context):
    """
    :type context: behave.runner.Context
    """
    print "pushed my card\n"


@when("I enter my PIN {pin}")
def step_impl2(context, pin):
    """
    :type context: behave.runner.Context
    """
    print "enter my pin {}\n".format(pin)


@step('I press "OK"')
def step_impl3(context):
    """
    :type context: behave.runner.Context
    """
    print "print ok\n"


@then("I should see the main menu")
def step_impl4(context):
    """
    :type context: behave.runner.Context
    """
    print "I see the menu\n"


@given("I have authenticate with correct pin {}")
def step_impl5(context, pin):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(u'''
        Given I have pushed my card in the slot
        When I enter my PIN %s
            And I press "OK"
    ''' % pin)


@given("I fill the data users")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.info("This is a test")
    for row in context.table:
        print row
        print 'name: ' + row['user']
        # assert (context.admin_user).to_equal(row['user'])


@when("I enter create user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@then("The user created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
