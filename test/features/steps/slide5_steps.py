from behave import given, when, then
import requests
import json


@given(u'I have created a new project')
def step_create_project(context):
    print(u'STEP: Given I have created a new project')

    url = 'https://www.pivotaltracker.com/services/v5/projects/2230988 | python -m json.tool'
    headers = {'X-TrackerToken': '566c34917ebf39c315d47cd9f2dcd1b5'}
    r = requests.get(url, headers=headers)
    print("CONTENT \n", r.content)
    print("CODE \n", r.status_code)


@then(u'I edit the project')
def step_edit_project(context):
    print(u'STEP: The I edit the project')

    payload = {'name': 'gdurannewname2test'}
    url = 'https://www.pivotaltracker.com/services/v5/projects/2230988 | python -m json.tool'
    headers = {'X-TrackerToken': '566c34917ebf39c315d47cd9f2dcd1b5'}
    r = requests.put(url, headers=headers, data=payload)
    print("CONTENT \n", r.content)
    print("CODE \n", r.status_code)



