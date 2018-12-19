import pprint

import requests
from behave import *

from src.pivotal_services.project import Projects

project = Projects()
response = []


@given('we have behave installed')
def step_impl1(context):
    pass


@when('we implement a test')
def step_imp12(context):
    assert True is not False


@then('behave will test it for us!')
def step_imp3(context):
    assert context.failed is False


@given("I create a new projet")
def step_i_create_a_new_project(context):
    """
    :type context: behave.runner.Context
    """
    project_name = 'test'
    response = project.create_project(project_name)
    # headers = {'X-TrackerToken': context.api_token}
    # data = {'name': project_name}
    # response = requests.post(context.url, headers=headers, data=data)
    assert project_name in response.text


@then("I get the project created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    headers = {'X-TrackerToken': context.api_token}
    response = requests.get(context.url, headers=headers)
    assert response


@when("I edit the project")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I edit the project')


@then("Prject should be update")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Prject should be update')
